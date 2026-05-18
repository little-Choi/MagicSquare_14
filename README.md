# MagicSquare

MagicSquare는 마방진 생성과 검증 로직을 ECB(Entity-Control-Boundary)
패턴과 TDD 흐름에 맞춰 구성하기 위한 프로젝트입니다.

## 현재 구성

```text
.
|-- .cursor/
|   `-- rules/
|       |-- *.mdc
|       `-- cpp/
|           `-- *.mdc
|-- entity/
|   |-- __init__.py
|   `-- user.py
|-- tests/
|   `-- entity/
|       `-- test_user.py
|-- Report/
|   `-- cursor_rules_report.md
|-- .cursorrules
`-- README.md
```

## 개발 규칙

- Python 코드는 PEP8, 타입힌트, Google 스타일 docstring을 따른다.
- 아키텍처는 ECB 패턴을 기준으로 한다.
- 테스트는 red, green, refactor 순서의 TDD 흐름을 따른다.
- Cursor 규칙은 `.cursor/rules` 아래의 `.mdc` 파일을 기준으로 관리한다.
- C++용 Cursor 규칙은 `.cursor/rules/cpp` 아래에 분리되어 있다.

## 테스트

Python 테스트는 `pytest`를 기준으로 작성한다.

```bash
python -m pytest
```

현재 환경에 `pytest`가 설치되어 있지 않다면 먼저 설치가 필요하다.

```bash
python -m pip install pytest
```
