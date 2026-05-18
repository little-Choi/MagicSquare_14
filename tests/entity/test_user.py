import pytest

from entity.user import User


VALID_USER_ID = 1
VALID_USER_NAME = "  Ada Lovelace  "
NORMALIZED_USER_NAME = "Ada Lovelace"
INVALID_USER_ID = 0
EMPTY_USER_NAME = "   "


def test_user_creation_normalizes_name() -> None:
    """User 생성 시 이름 양끝 공백을 제거한다."""
    # Arrange & Act
    user = User(user_id=VALID_USER_ID, name=VALID_USER_NAME)

    # Assert
    assert user.user_id == VALID_USER_ID
    assert user.name == NORMALIZED_USER_NAME


def test_user_rejects_non_positive_user_id() -> None:
    """User id는 양수여야 한다."""
    # Arrange, Act & Assert
    with pytest.raises(ValueError, match="user_id"):
        User(user_id=INVALID_USER_ID, name=VALID_USER_NAME)


def test_user_rejects_empty_name() -> None:
    """User 이름은 비어 있을 수 없다."""
    # Arrange, Act & Assert
    with pytest.raises(ValueError, match="name"):
        User(user_id=VALID_USER_ID, name=EMPTY_USER_NAME)
