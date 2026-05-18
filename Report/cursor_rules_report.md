# MagicSquare Cursor Rules Report

## 개요

MagicSquare 프로젝트의 Cursor 규칙 파일을 `.cursorrules`에서
`.cursor/rules` 기반의 `.mdc` 파일 구조로 확장했다.

이후 C++ 작업을 위한 별도 규칙 세트를 `.mdc` 형식으로 작성하고,
`.cursor/rules/cpp` 폴더 안으로 이동했다.

## 현재 규칙 파일 구조

```text
.cursor/
`-- rules/
    |-- magicsquare-project.mdc
    |-- magicsquare-python-code-style.mdc
    |-- magicsquare-ecb-architecture.mdc
    |-- magicsquare-tdd-testing.mdc
    |-- magicsquare-forbidden.mdc
    `-- cpp/
        |-- magicsquare-cpp-project.mdc
        |-- magicsquare-cpp-code-style.mdc
        |-- magicsquare-cpp-ecb-architecture.mdc
        |-- magicsquare-cpp-tdd-testing.mdc
        `-- magicsquare-cpp-forbidden.mdc
```

## Python 규칙 세트

- MagicSquare 프로젝트 목표와 AI 행동 규칙을 정의했다.
- Python 코드 스타일 규칙을 분리했다.
- ECB 아키텍처 규칙을 분리했다.
- TDD 및 pytest 테스트 규칙을 분리했다.
- 금지 패턴과 대안을 별도 규칙으로 분리했다.

## C++ 규칙 세트

- C++20 이상 기준의 MagicSquare 규칙을 작성했다.
- RAII, const-correctness, 소유권, 헤더/소스 분리 규칙을 포함했다.
- ECB 계층 구조를 C++ 폴더 기준으로 재정의했다.
- C++ 테스트 규칙과 TDD 흐름을 정의했다.
- `std::cout` 남용, 매직 넘버, `catch (...)`, 원시 owning pointer,
  헤더의 `using namespace std;` 같은 금지 패턴을 명시했다.

## 검증 결과

- `.cursor/rules` 아래에 Python용 `.mdc` 파일 5개가 존재한다.
- `.cursor/rules/cpp` 아래에 C++용 `.mdc` 파일 5개가 존재한다.
- C++ 규칙은 `.cpp` 소스 파일이 아니라 Cursor Rule용 `.mdc` 형식으로 작성되었다.
- 최근 확인 시 규칙 파일에 linter 진단 오류는 없었다.

## 참고 사항

- 기존 `.cursorrules` 파일은 유지되어 있다.
- 향후 Cursor의 최신 규칙 방식만 사용하려면 `.cursor/rules`의 `.mdc` 파일을
  기준으로 관리하는 것이 적합하다.
