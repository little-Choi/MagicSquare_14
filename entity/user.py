from dataclasses import dataclass


MIN_USER_ID = 1


@dataclass(frozen=True)
class User:
    """MagicSquare 사용자를 표현하는 Entity 클래스.

    Attributes:
        user_id: 사용자를 식별하는 양의 정수 id.
        name: 앞뒤 공백이 제거된 사용자 이름.
    """

    user_id: int
    name: str

    def __post_init__(self) -> None:
        """User 생성 직후 도메인 불변 조건을 검증한다.

        Raises:
            ValueError: user_id가 양수가 아니거나 name이 비어 있는 경우.
        """
        normalized_name = self.name.strip()

        if self.user_id < MIN_USER_ID:
            raise ValueError("user_id must be a positive integer.")

        if not normalized_name:
            raise ValueError("name must not be empty.")

        object.__setattr__(self, "name", normalized_name)
