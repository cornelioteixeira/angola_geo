"""
Exemplo de uso da biblioteca angola_geo.

Este script demonstra todas as funcionalidades principais da biblioteca.
"""

from angola_geo import AngolaGeo, ProvinciaInexistente


def main():
    # Inicializar a biblioteca
    geo = AngolaGeo()
    
    print("=" * 60)
    print("Angola Geo - Exemplo de Uso")
    print("=" * 60)
    print()
    
    # 1. Obter metadados
    print("1. Metadados do Conjunto de Dados")
    print("-" * 60)
    metadados = geo.obter_metadados()
    print(f"Lei: {metadados['law']}")
    print(f"Data de Vigência: {metadados['effective_date']}")
    print(f"Total de Províncias: {metadados['total_provinces']}")
    print(f"Total de Municípios: {metadados['total_municipalities']}")
    print(f"Total de Comunas: {metadados['total_communes']}")
    print()
    
    # 2. Listar todas as províncias
    print("2. Todas as Províncias")
    print("-" * 60)
    provincias = geo.listar_provincias()
    print(f"Encontradas {len(provincias)} províncias:")
    for provincia in provincias[:5]:  # Mostrar primeiras 5
        print(f"  - {provincia['nome']} (Capital: {provincia['capital']}, "
              f"Municípios: {provincia['total_municipios']})")
    print(f"  ... e mais {len(provincias) - 5}")
    print()
    
    # 3. Obter uma província específica
    print("3. Província Específica - Luanda")
    print("-" * 60)
    luanda = geo.obter_provincia("Luanda")
    print(f"Nome: {luanda['nome']}")
    print(f"Capital: {luanda['capital']}")
    print(f"Total de Municípios: {luanda['total_municipios']}")
    print(f"Municípios: {', '.join([m['nome'] for m in luanda['municipios'][:5]])}...")
    print()
    
    # 4. Listar municípios de uma província
    print("4. Municípios de Luanda")
    print("-" * 60)
    municipios_luanda = geo.listar_municipios(provincia="Luanda")
    print(f"Encontrados {len(municipios_luanda)} municípios:")
    for muni in municipios_luanda[:8]:  # Mostrar primeiros 8
        print(f"  - {muni['nome']}")
    print(f"  ... e mais {len(municipios_luanda) - 8}")
    print()
    
    # 5. Listar todos os municípios
    print("5. Todos os Municípios (com dados)")
    print("-" * 60)
    todos_municipios = geo.listar_municipios()
    municipios_com_nomes = [m for m in todos_municipios if m['nome']]
    print(f"Total de municípios com nomes: {len(municipios_com_nomes)}")
    print(f"Total esperado: {geo.contar_municipios()}")
    print(f"Cobertura: {len(municipios_com_nomes)}/{geo.contar_municipios()} "
          f"({len(municipios_com_nomes)/geo.contar_municipios()*100:.1f}%)")
    print()
    
    # 6. Obter províncias novas
    print("6. Províncias Novas (Criadas pela Lei 14/24)")
    print("-" * 60)
    provincias_novas = geo.obter_provincias_novas()
    for provincia in provincias_novas:
        print(f"  - {provincia['nome']} (Capital: {provincia['capital']})")
        if 'observacoes' in provincia:
            print(f"    {provincia['observacoes']}")
    print()
    
    # 7. Funcionalidade de pesquisa
    print("7. Pesquisar por 'Bengo'")
    print("-" * 60)
    resultados = geo.pesquisar("Bengo")
    print(f"Províncias encontradas: {len(resultados['provincias'])}")
    for prov in resultados['provincias']:
        print(f"  - {prov['nome']}")
    print(f"Municípios encontrados: {len(resultados['municipios'])}")
    for muni in resultados['municipios'][:3]:
        print(f"  - {muni['nome']} ({muni['provincia']})")
    print()
    
    # 8. Obter apenas nomes das províncias
    print("8. Lista Simples de Nomes das Províncias")
    print("-" * 60)
    nomes_provincias = geo.obter_nomes_provincias()
    print(", ".join(nomes_provincias))
    print()
    
    # 9. Tratamento de erros
    print("9. Tratamento de Erros")
    print("-" * 60)
    try:
        geo.obter_provincia("ProvinciaInexistente")
    except ProvinciaInexistente as e:
        print(f"Erro capturado conforme esperado: {e}")
    print()
    
    # 10. Contagem de municípios
    print("10. Contagem de Municípios")
    print("-" * 60)
    print(f"Total de municípios: {geo.contar_municipios()}")
    print(f"Municípios de Luanda: {geo.contar_municipios('Luanda')}")
    print(f"Municípios de Bengo: {geo.contar_municipios('Bengo')}")
    print(f"Municípios de Icolo e Bengo: {geo.contar_municipios('Icolo e Bengo')}")
    print()
    
    print("=" * 60)
    print("Exemplo concluído com sucesso!")
    print("=" * 60)


if __name__ == "__main__":
    main()
