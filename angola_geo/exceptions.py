"""Custom exceptions for the angola_geo library."""


class AngolaGeoError(Exception):
    """Base exception for angola_geo library."""
    pass


class ProvinceNotFoundError(AngolaGeoError):
    """Raised when a province is not found."""
    
    def __init__(self, province_name: str):
        self.province_name = province_name
        super().__init__(f"Province '{province_name}' not found")


class MunicipalityNotFoundError(AngolaGeoError):
    """Raised when a municipality is not found."""
    
    def __init__(self, municipality_name: str):
        self.municipality_name = municipality_name
        super().__init__(f"Municipality '{municipality_name}' not found")


class InvalidDataError(AngolaGeoError):
    """Raised when data validation fails."""
    pass
