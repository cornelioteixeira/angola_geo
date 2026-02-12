# Angola Geo - Referências

Este documento lista todas as fontes oficiais e referências utilizadas na construção da biblioteca Angola Geo.

## Legislação Oficial

### Lei n.º 14/24 - Lei Principal

**Título Completo:** Lei n.º 14/24, de 5 de Setembro - Divisão Político-Administrativa da República de Angola

**Publicação:**
- **Diário da República:** Iª Série, n.º 171
- **Data de Publicação:** 5 de Setembro de 2024
- **Data de Vigência:** 1 de Janeiro de 2025

**Conteúdo:**
- Estabelece a nova divisão político-administrativa de Angola
- Define as 21 províncias (incluindo 3 novas)
- Estabelece os 326 municípios
- Define as 378 comunas/distritos

**Referência Oficial:**
```
Lei n.º 14/24
Diário da República Iª Série n.º 171
5 de Setembro de 2024
República de Angola
```

**Principais Mudanças:**
- Criação de 3 novas províncias:
  - **Icolo e Bengo** (separada de Luanda) - Capital: Catete
  - **Cuando** (separada de Cuando Cubango) - Capital: Mavinga
  - **Moxico Leste** (separada de Moxico) - Capital: Cazombo
- Aumento de 18 para 21 províncias
- Aumento de 164 para 326 municípios
- Reestruturação das comunas/distritos

---

## Fontes Governamentais

### Ministério da Administração do Território (MAT)

**Website Oficial:** [governo.gov.ao](https://governo.gov.ao)

**Responsabilidades:**
- Administração territorial de Angola
- Implementação da Lei 14/24
- Dados oficiais sobre divisões administrativas

**Informações Fornecidas:**
- Estrutura administrativa das províncias
- Limites territoriais
- Capitais provinciais e municipais

---

### Diário da República

**Descrição:** Publicação oficial do Estado Angolano

**Relevância:**
- Fonte primária para legislação
- Publicação oficial da Lei 14/24
- Documentação legal autêntica

**Acesso:**
- Edições físicas em instituições governamentais
- Versões digitais através de canais oficiais

---

## Fontes de Dados Estatísticos

### Instituto Nacional de Estatística (INE)

**Website:** [ine.gov.ao](https://www.ine.gov.ao)

**Dados Relevantes:**
- Censos populacionais
- Estatísticas por província e município
- Dados demográficos

**Uso Futuro:**
- População por província/município
- Densidade populacional
- Dados socioeconômicos

---

## Estrutura de Dados

### Hierarquia Administrativa

```
República de Angola
├── Províncias (21)
│   ├── Municípios (326 total)
│   │   └── Comunas/Distritos (378 total)
```

### Comparação Histórica

| Aspecto | Antes (Lei Anterior) | Depois (Lei 14/24) |
|---------|---------------------|-------------------|
| Províncias | 18 | 21 |
| Municípios | 164 | 326 |
| Comunas | Variável | 378 |

---

## Províncias de Angola (Lei 14/24)

### Lista Completa

1. **Bengo** - Capital: Dande
2. **Benguela** - Capital: Benguela
3. **Bié** - Capital: Cuíto
4. **Cabinda** - Capital: Cabinda
5. **Cuando** - Capital: Mavinga ⭐ *Nova*
6. **Cuanza Norte** - Capital: N'dalatando
7. **Cuanza Sul** - Capital: Sumbe
8. **Cubango** - Capital: Menongue
9. **Cunene** - Capital: Ondjiva
10. **Huambo** - Capital: Huambo
11. **Huíla** - Capital: Lubango
12. **Icolo e Bengo** - Capital: Catete ⭐ *Nova*
13. **Luanda** - Capital: Ingombota
14. **Lunda Norte** - Capital: Dundo
15. **Lunda Sul** - Capital: Saurimo
16. **Malanje** - Capital: Malanje
17. **Moxico** - Capital: Luena
18. **Moxico Leste** - Capital: Cazombo ⭐ *Nova*
19. **Namibe** - Capital: Moçâmedes
20. **Uíge** - Capital: Uíge
21. **Zaire** - Capital: M'banza Congo

---

## Metodologia de Coleta de Dados

### Fontes Primárias
1. **Lei n.º 14/24** - Base legal oficial
2. **Diário da República** - Publicação oficial
3. **MAT** - Dados administrativos

### Fontes Secundárias
1. **INE** - Dados estatísticos
2. **Websites governamentais provinciais**
3. **Documentação oficial de municípios**

### Processo de Verificação
1. Cruzamento de múltiplas fontes oficiais
2. Verificação de consistência dos dados
3. Validação com documentação legal
4. Atualização contínua conforme novas informações

---

## Dados Futuros Planejados

### Coordenadas Geográficas
- **Fonte Planejada:** INE, Google Maps API, OpenStreetMap
- **Formato:** Latitude/Longitude (decimal)
- **Precisão:** Centro administrativo de cada divisão

### População
- **Fonte Planejada:** INE (Censo 2024/2025)
- **Dados:** População total por província/município
- **Atualização:** Conforme censos oficiais

### Área/Tamanho
- **Fonte Planejada:** INE, MAT
- **Unidade:** Quilômetros quadrados (km²)
- **Dados:** Área territorial de cada divisão

### Códigos Postais
- **Fonte Planejada:** Correios de Angola
- **Formato:** Código postal por município/comuna
- **Estrutura:** Sistema de códigos postais angolano

---

## Citação da Biblioteca

### Formato APA
```
Teixeira, C. (2026). Angola Geo: Biblioteca Python para divisões administrativas de Angola 
(Versão 0.2.0) [Software]. https://github.com/yourusername/geolocation-ao
```

### Formato BibTeX
```bibtex
@software{angola_geo,
  author = {Teixeira, Cornelio},
  title = {Angola Geo: Biblioteca Python para divisões administrativas de Angola},
  year = {2026},
  version = {0.2.0},
  url = {https://github.com/yourusername/geolocation-ao},
  note = {Baseado na Lei n.º 14/24, de 5 de Setembro de 2024}
}
```

---

## Disclaimer / Aviso Legal

Esta biblioteca é um projeto independente e não é oficialmente afiliada ao Governo de Angola, ao Ministério da Administração do Território, ou qualquer outra entidade governamental.

Os dados são coletados de fontes públicas oficiais e são fornecidos "como estão" para fins informativos e de desenvolvimento. Para uso oficial ou legal, sempre consulte as fontes governamentais primárias.

---

## Atualizações e Manutenção

**Responsável:** Cornelio Teixeira  
**Última Atualização:** 12 de Fevereiro de 2026  
**Versão dos Dados:** 0.2.0  
**Base Legal:** Lei n.º 14/24 (vigente desde 1 de Janeiro de 2025)

---

## Contribuições

Se você tem acesso a fontes oficiais adicionais ou dados verificados, por favor contribua através de:
- Pull requests no GitHub
- Issues com referências documentadas
- Contato direto com documentação comprobatória

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.

---

## Links Úteis

- **Governo de Angola:** https://governo.gov.ao
- **INE Angola:** https://www.ine.gov.ao
- **Diário da República:** Disponível através de canais oficiais
- **Repositório GitHub:** https://github.com/yourusername/geolocation-ao

---

**Última Revisão:** 12 de Fevereiro de 2026
