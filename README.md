# shared-libs

Shared libraries and internal SDKs

## Getting Started

### Prerequisites
- Docker >= 20.10
- Make

### Installation
```bash
make install
make dev
```

### Testing
```bash
make test
make lint
```

## Architecture

This service follows a clean architecture pattern with:
- **API layer** - HTTP/gRPC handlers
- **Service layer** - Business logic
- **Repository layer** - Data access

## Contributing

1. Fork the repo
2. Create your feature branch
3. Submit a PR with tests

## License

MIT
