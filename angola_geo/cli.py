#!/usr/bin/env python3
"""
CLI para Angola Geo - Ferramenta de linha de comando para consultas rápidas.

Uso:
    angola-geo listar provincias
    angola-geo obter provincia <nome>
    angola-geo listar municipios [--provincia <nome>]
    angola-geo pesquisar <termo>
    angola-geo info
"""

import sys
import argparse
import json
from typing import Optional
from angola_geo import AngolaGeo, ProvinciaInexistente


def formatar_provincia(provincia: dict, detalhado: bool = False) -> str:
    """Formata dados de uma província para exibição."""
    resultado = f"\n📍 {provincia['nome']}"
    resultado += f"\n   Capital: {provincia['capital']}"
    resultado += f"\n   Municípios: {provincia['total_municipios']}"
    
    if detalhado and provincia['municipios']:
        resultado += f"\n   Lista de Municípios:"
        for muni in provincia['municipios']:
            resultado += f"\n     • {muni['nome']}"
    
    if 'observacoes' in provincia:
        resultado += f"\n   ℹ️  {provincia['observacoes']}"
    
    return resultado


def formatar_municipio(municipio: dict) -> str:
    """Formata dados de um município para exibição."""
    return f"  • {municipio['nome']} ({municipio['provincia']})"


def cmd_listar_provincias(args, geo: AngolaGeo):
    """Lista todas as províncias."""
    provincias = geo.listar_provincias()
    
    print(f"\n🇦🇴 Angola - {len(provincias)} Províncias\n")
    print("=" * 60)
    
    for provincia in provincias:
        print(formatar_provincia(provincia, detalhado=args.detalhado))
    
    print("\n" + "=" * 60)
    print(f"Total: {len(provincias)} províncias, {geo.contar_municipios()} municípios")


def cmd_obter_provincia(args, geo: AngolaGeo):
    """Obtém detalhes de uma província específica."""
    try:
        provincia = geo.obter_provincia(args.nome)
        
        print(f"\n🇦🇴 Província de {provincia['nome']}")
        print("=" * 60)
        print(formatar_provincia(provincia, detalhado=True))
        print("=" * 60)
        
    except ProvinciaInexistente as e:
        print(f"\n❌ Erro: {e}")
        print(f"\n💡 Dica: Use 'angola-geo listar provincias' para ver todas as províncias disponíveis")
        sys.exit(1)


def cmd_listar_municipios(args, geo: AngolaGeo):
    """Lista municípios, opcionalmente filtrados por província."""
    try:
        if args.provincia:
            municipios = geo.listar_municipios(provincia=args.provincia)
            titulo = f"Municípios de {args.provincia}"
        else:
            municipios = geo.listar_municipios()
            titulo = "Todos os Municípios"
        
        # Filtrar apenas municípios com nomes
        municipios_com_nomes = [m for m in municipios if m['nome']]
        
        print(f"\n🏘️  {titulo}")
        print("=" * 60)
        
        if not municipios_com_nomes:
            print("\n⚠️  Dados de municípios ainda não disponíveis para esta província.")
        else:
            for muni in municipios_com_nomes:
                print(formatar_municipio(muni))
        
        print("\n" + "=" * 60)
        print(f"Total: {len(municipios_com_nomes)} municípios com dados")
        
        if args.provincia:
            total_esperado = geo.contar_municipios(args.provincia)
            if len(municipios_com_nomes) < total_esperado:
                print(f"⏳ Cobertura: {len(municipios_com_nomes)}/{total_esperado} ({len(municipios_com_nomes)/total_esperado*100:.1f}%)")
        
    except ProvinciaInexistente as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)


def cmd_pesquisar(args, geo: AngolaGeo):
    """Pesquisa por termo em todas as divisões."""
    resultados = geo.pesquisar(args.termo)
    
    print(f"\n🔍 Resultados para '{args.termo}'")
    print("=" * 60)
    
    total = sum(len(v) for v in resultados.values())
    
    if total == 0:
        print("\n❌ Nenhum resultado encontrado.")
    else:
        if resultados['provincias']:
            print(f"\n📍 Províncias ({len(resultados['provincias'])}):")
            for prov in resultados['provincias']:
                print(f"  • {prov['nome']} (Capital: {prov['capital']})")
        
        if resultados['municipios']:
            print(f"\n🏘️  Municípios ({len(resultados['municipios'])}):")
            for muni in resultados['municipios']:
                print(f"  • {muni['nome']} - {muni['provincia']}")
        
        if resultados['comunas']:
            print(f"\n🏡 Comunas ({len(resultados['comunas'])}):")
            for comuna in resultados['comunas']:
                print(f"  • {comuna['nome']} ({comuna['municipio']}, {comuna['provincia']})")
    
    print("\n" + "=" * 60)
    print(f"Total: {total} resultados encontrados")


def cmd_info(args, geo: AngolaGeo):
    """Exibe informações sobre o dataset."""
    meta = geo.obter_metadados()
    
    print("\n🇦🇴 Angola Geo - Informações do Dataset")
    print("=" * 60)
    print(f"\n📜 Lei: {meta['law']}")
    print(f"📅 Data de Publicação: {meta['publication_date']}")
    print(f"✅ Data de Vigência: {meta['effective_date']}")
    print(f"\n📊 Estatísticas:")
    print(f"   • Províncias: {meta['total_provinces']}")
    print(f"   • Municípios: {meta['total_municipalities']}")
    print(f"   • Comunas: {meta['total_communes']}")
    
    print(f"\n📈 Mudanças:")
    print(f"   • Províncias anteriores: {meta['previous_provinces']}")
    print(f"   • Municípios anteriores: {meta['previous_municipalities']}")
    
    # Mostrar províncias novas
    novas = geo.obter_provincias_novas()
    print(f"\n🆕 Novas Províncias ({len(novas)}):")
    for prov in novas:
        print(f"   • {prov['nome']} (Capital: {prov['capital']})")
    
    print(f"\n📚 Fontes:")
    for fonte in meta['sources']:
        print(f"   • {fonte}")
    
    print(f"\n🔄 Versão dos Dados: {meta['data_version']}")
    print(f"📅 Última Atualização: {meta['last_updated']}")
    
    print("\n" + "=" * 60)


def cmd_provincias_novas(args, geo: AngolaGeo):
    """Lista as três novas províncias criadas pela Lei 14/24."""
    novas = geo.obter_provincias_novas()
    
    print("\n🆕 Novas Províncias - Lei 14/24")
    print("=" * 60)
    
    for provincia in novas:
        print(formatar_provincia(provincia, detalhado=True))
    
    print("\n" + "=" * 60)
    print(f"Total: {len(novas)} novas províncias")


def main():
    """Função principal da CLI."""
    parser = argparse.ArgumentParser(
        description='Angola Geo - Consultas sobre divisões administrativas de Angola',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  angola-geo listar provincias
  angola-geo obter provincia Luanda
  angola-geo listar municipios --provincia Luanda
  angola-geo pesquisar Bengo
  angola-geo info
  angola-geo novas
        """
    )
    
    subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')
    
    # Comando: listar
    listar_parser = subparsers.add_parser('listar', help='Lista províncias ou municípios')
    listar_subparsers = listar_parser.add_subparsers(dest='tipo')
    
    # listar provincias
    provincias_parser = listar_subparsers.add_parser('provincias', help='Lista todas as províncias')
    provincias_parser.add_argument('-d', '--detalhado', action='store_true',
                                   help='Mostrar lista de municípios para cada província')
    
    # listar municipios
    municipios_parser = listar_subparsers.add_parser('municipios', help='Lista municípios')
    municipios_parser.add_argument('-p', '--provincia', type=str,
                                   help='Filtrar por província')
    
    # Comando: obter
    obter_parser = subparsers.add_parser('obter', help='Obtém detalhes de uma província')
    obter_subparsers = obter_parser.add_subparsers(dest='tipo')
    
    # obter provincia
    provincia_parser = obter_subparsers.add_parser('provincia', help='Obtém detalhes de uma província')
    provincia_parser.add_argument('nome', type=str, help='Nome da província')
    
    # Comando: pesquisar
    pesquisar_parser = subparsers.add_parser('pesquisar', help='Pesquisa por termo')
    pesquisar_parser.add_argument('termo', type=str, help='Termo de pesquisa')
    
    # Comando: info
    subparsers.add_parser('info', help='Informações sobre o dataset')
    
    # Comando: novas
    subparsers.add_parser('novas', help='Lista as novas províncias criadas pela Lei 14/24')
    
    # Parse argumentos
    args = parser.parse_args()
    
    if not args.comando:
        parser.print_help()
        sys.exit(0)
    
    # Inicializar AngolaGeo
    geo = AngolaGeo()
    
    # Executar comando
    try:
        if args.comando == 'listar':
            if args.tipo == 'provincias':
                cmd_listar_provincias(args, geo)
            elif args.tipo == 'municipios':
                cmd_listar_municipios(args, geo)
            else:
                listar_parser.print_help()
        
        elif args.comando == 'obter':
            if args.tipo == 'provincia':
                cmd_obter_provincia(args, geo)
            else:
                obter_parser.print_help()
        
        elif args.comando == 'pesquisar':
            cmd_pesquisar(args, geo)
        
        elif args.comando == 'info':
            cmd_info(args, geo)
        
        elif args.comando == 'novas':
            cmd_provincias_novas(args, geo)
        
        else:
            parser.print_help()
    
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
