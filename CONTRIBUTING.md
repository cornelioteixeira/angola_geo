# Contributing to Angola Geo

Thank you for your interest in contributing to the Angola Geo library! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:
1. Check if the issue already exists in the issue tracker
2. If not, create a new issue with:
   - Clear description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (Python version, OS, etc.)

### Contributing Data

The most valuable contribution is adding missing municipality and commune data!

#### Adding Municipality Names

1. Find official sources for municipality data (Lei 14/24, government websites, etc.)
2. Update `angola_geo/data/divisions.json`:
   ```json
   {
     "name": "Province Name",
     "municipalities": [
       {"name": "Municipality Name", "communes": []}
     ]
   }
   ```
3. Verify the data is accurate
4. Update the data coverage in README.md
5. Submit a pull request

#### Adding Commune Data

1. Research commune names for municipalities
2. Add to the `communes` array in `divisions.json`:
   ```json
   {
     "name": "Municipality Name",
     "communes": [
       {"name": "Commune Name"},
       {"name": "Another Commune"}
     ]
   }
   ```
3. Submit a pull request

### Code Contributions

#### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/geolocation-ao.git
cd geolocation-ao

# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install in development mode
pip install -e .
```

#### Running Tests

```bash
# Run all tests
python3 -m unittest discover tests/

# Run specific test file
python3 -m unittest tests/test_angola_geo.py

# Run with verbose output
python3 -m unittest tests/test_angola_geo.py -v
```

#### Code Style

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions focused and single-purpose (SOLID principles)
- Avoid code duplication (DRY principle)

#### Adding New Features

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Implement your feature
3. Add tests for your feature
4. Update documentation (README.md, docstrings)
5. Ensure all tests pass
6. Submit a pull request

### Pull Request Process

1. **Fork** the repository
2. **Create a branch** for your changes
3. **Make your changes** following the code style guidelines
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Run tests** to ensure everything works
7. **Commit** with clear, descriptive messages
8. **Push** to your fork
9. **Submit a pull request** with:
   - Clear description of changes
   - Reference to any related issues
   - Screenshots/examples if applicable

### Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add municipality data for Benguela province

- Added all 23 municipalities for Benguela
- Verified data against Lei 14/24
- Updated README with new coverage stats
```

### Data Sources

When adding data, always cite your sources:
- Lei n.º 14/24 (primary source)
- Official government websites (governo.gov.ao, mat.gov.ao)
- Instituto Nacional de Estatística (INE)
- Official provincial government sites

**Never use**:
- Unverified Wikipedia data
- Unofficial blogs or forums
- Outdated sources (pre-2024)

## Development Priorities

### High Priority
1. Adding remaining municipality names (291 municipalities)
2. Adding commune data (378 communes)
3. Verifying existing data accuracy

### Medium Priority
1. Adding geographic coordinates
2. Adding population data
3. Adding area/size information

### Low Priority
1. CLI tool
2. REST API wrapper
3. Additional metadata

## Questions?

If you have questions about contributing:
- Open an issue with the "question" label
- Check existing issues and pull requests
- Review the README.md and documentation

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Prioritize data accuracy and quality

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for helping make Angola Geo better! 🇦🇴
