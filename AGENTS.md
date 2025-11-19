# AGENTS.md

This file tracks AI agent contributions to the ddd-physical-units project.

## About This Project

**ddd-physical-units** is a Python library for supporting units of measurement in Domain-Driven Design (DDD). The library provides a base class for physical units with type safety and a clean API.

## Recent Agent Sessions

### Session 2025-11-19: Project Documentation

**Agent**: Continue CLI  
**Co-Author**: shmakovpn

#### Changes
- Created initial AGENTS.md file to track AI contributions
- Documented project structure and recent development history

---

## Project History (Human-Driven Development)

### 2025-11-17: Repository Setup and Testing Infrastructure

**Author**: shmakovpn

#### PR #3: README Badges
- Added CI/CD status badge for GitHub Actions
- Added codecov badge for test coverage tracking
- Added PyPI version badge
- Added download statistics badge from pepy.tech
- Added Python versions compatibility badge

#### PR #2: Testing Infrastructure
- Created comprehensive pytest structure for `__all__` attribute validation
- Implemented `import_all_python_modules` fixture for dynamic module testing
- Added unit tests for `BasePhysicalUnit`
- Configured pytest with proper test discovery settings

#### PR #1: Code Quality Setup
- Configured Ruff linter for Python code quality
- Set line length to 120 characters
- Configured VS Code settings for development workflow
- Added branch protection to prevent direct pushes to `main`

### 2025-11-16: Core Implementation

**Author**: shmakovpn

#### Package Configuration
- Set up modern Python packaging with `pyproject.toml`
- Configured setuptools with `src/` layout
- Added MIT License
- Created GitHub Actions CI/CD pipeline with:
  - Multi-version Python testing (3.9, 3.10, 3.11, 3.12, 3.13)
  - Test coverage reporting to codecov
  - Automated testing on push and pull requests
- Established requirements structure (development and production)
- Added basic pytest configuration

#### Core Features
- Implemented `BasePhysicalUnit` dataclass with:
  - `value` field supporting int, float, and complex numbers
  - `label` field for unit abbreviation (e.g., "m" for meters)
  - Type hints and documentation
  - Proper `__all__` export

### 2023-07-20: Initial Commit

**Author**: shmakovpn

- Created repository with basic README
- Established project vision for DDD physical units support

---

## Development Standards

### Testing
- All Python modules must define `__all__` for explicit exports
- Unit tests required for new physical unit types
- Pytest fixtures available for module import validation
- Target: High test coverage tracked via codecov

### Code Quality
- Ruff linter enforced for all Python code
- Type hints required for public APIs
- Line length: 120 characters maximum
- Branch protection: No direct pushes to `main`

### CI/CD
- GitHub Actions runs tests on all PRs
- Multi-version Python support (3.9+)
- Automated coverage reporting
- All checks must pass before merge

---

## Future Directions

### Potential Enhancements
- Implement specific unit types (Length, Mass, Time, etc.)
- Add unit conversion functionality
- Support for derived units (velocity, acceleration, etc.)
- Dimensional analysis validation
- Support for unit arithmetic and operations
- International System of Units (SI) support
- Imperial/US customary units support

### Testing Enhancements
- Property-based testing for unit conversions
- Performance benchmarks
- Integration tests for complex unit operations

---

## Contributing

This project welcomes contributions from both humans and AI agents. When committing changes:

1. All commits must include proper co-authorship:
   ```
   Co-authored-by: shmakovpn <shmakovpn@yandex.ru>
   ```

2. For AI agent contributions, include in commit messages:
   ```
   Generated with Continue (https://continue.dev)
   Co-Authored-By: Continue <noreply@continue.dev>
   ```

3. Pull requests by agents should include:
   ```
   This agent session was co-authored by shmakovpn and Continue (https://continue.dev).
   ```

---

**Last Updated**: 2025-11-19  
**Updated By**: Continue CLI Agent
