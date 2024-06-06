from asyncio import sleep


async def send_email(
        send_to: str,
        subject: str,
        text: str,
):
    print(send_to, subject, text)
    await sleep(1)
    print("email sent")
