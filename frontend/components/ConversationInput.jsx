
function ConversationInput({ conversation, setConversation }) {
    const handleChange = (e) => {
        const lines = e.target.value.split('\n')
        setConversation(lines)
    }

    return (
        <div className="conversation-input">
            <h3>Conversation</h3>
            <textarea
                value={conversation.join('\n')}
                onChange={handleChange}
                placeholder="Enter conversation (one message per line)"
                rows={8}
            />
            <p className="hint">{conversation.length} messages</p>
        </div>
    )
}

export default ConversationInput