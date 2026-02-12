"""Exceções customizadas para a biblioteca angola_geo."""


class ErroAngolaGeo(Exception):
    """Exceção base para a biblioteca angola_geo."""
    pass


class ProvinciaInexistente(ErroAngolaGeo):
    """Lançada quando uma província não é encontrada."""
    
    def __init__(self, nome_provincia: str):
        self.nome_provincia = nome_provincia
        super().__init__(f"Província '{nome_provincia}' não encontrada")


class MunicipioInexistente(ErroAngolaGeo):
    """Lançada quando um município não é encontrado."""
    
    def __init__(self, nome_municipio: str):
        self.nome_municipio = nome_municipio
        super().__init__(f"Município '{nome_municipio}' não encontrado")


class DadosInvalidos(ErroAngolaGeo):
    """Lançada quando a validação de dados falha."""
    pass
