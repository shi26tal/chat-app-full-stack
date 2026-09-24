from src import extensions

# save msg to db
# get msg for a room


class MessageRepository:

    @staticmethod
    def create(room_id, message_id, user_id, content, created_at):
        query = """
        INSERT INTO messages (
            room_id,
            message_id,
            user_id,
            content,
            created_at
        )
        VALUES (%s, %s, %s, %s, %s)
        """

        print(
            "Saving message:",
            room_id,
            message_id,
            user_id,
            content,
            created_at
        )

        extensions.cassandra_session.execute(
            query,
            (
                room_id,
                message_id,
                user_id,
                content,
                created_at
            )
        )

    @staticmethod
    def get_by_room(room_id):
        query = """
        SELECT
            room_id,
            message_id,
            user_id,
            content,
            created_at
        FROM messages
        WHERE room_id = %s
        ORDER BY created_at ASC
        """

        return extensions.cassandra_session.execute(
            query,
            (room_id,)
        )