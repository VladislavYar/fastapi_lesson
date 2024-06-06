import asyncio

from core.models import AccessPermisson, generate_token, db_helper


async def main():
    async with db_helper.async_session() as session:
        async with session.begin():
            access_read_users_a = AccessPermisson(action="USERS_GET")
            access_read_users_b = AccessPermisson(
                token=generate_token(),
                action="USER_GET",
            )
            access_write_users = AccessPermisson(
                token=access_read_users_b.token,
                action="USER_CREATE",
            )
            session.add_all(
                (
                    access_read_users_a,
                    access_read_users_b,
                    access_write_users,
                )
            )
    print("token a", repr(access_read_users_a.token))
    print("token b", repr(access_read_users_b.token))


if __name__ == "__main__":
    asyncio.run(main())
