from copilot.memory.in_memory import InMemoryConversationStore


def test_add_and_get_messages():
    """Test adding and retrieving messages."""

    store = InMemoryConversationStore()

    store.add_message(
        conversation_id="conv1",
        role="user",
        content="Hello",
    )

    store.add_message(
        conversation_id="conv1",
        role="assistant",
        content="Hi there!",
    )

    assert store.get_messages("conv1") == [
        {
            "role": "user",
            "content": "Hello",
        },
        {
            "role": "assistant",
            "content": "Hi there!",
        },
    ]


def test_empty_conversation():
    """Test retrieving messages from a new conversation."""

    store = InMemoryConversationStore()

    assert store.get_messages("new-conversation") == []


def test_clear_conversation():
    """Test clearing a conversation."""

    store = InMemoryConversationStore()

    store.add_message(
        conversation_id="conv1",
        role="user",
        content="Hello",
    )

    store.clear("conv1")

    assert store.get_messages("conv1") == []


def test_multiple_conversations():
    """Test conversations are isolated."""

    store = InMemoryConversationStore()

    store.add_message(
        conversation_id="conv1",
        role="user",
        content="First",
    )

    store.add_message(
        conversation_id="conv2",
        role="user",
        content="Second",
    )

    assert store.get_messages("conv1") == [
        {
            "role": "user",
            "content": "First",
        },
    ]

    assert store.get_messages("conv2") == [
        {
            "role": "user",
            "content": "Second",
        },
    ]


def test_clear_unknown_conversation():
    """Clearing an unknown conversation should not raise an error."""

    store = InMemoryConversationStore()

    store.clear("does-not-exist")

    assert store.get_messages("does-not-exist") == []