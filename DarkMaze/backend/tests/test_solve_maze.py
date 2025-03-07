import pytest
import httpx

USERNAME = "TestUser"
RESET_URL = f"http://127.0.0.1:8000/api/v1/reset?username={USERNAME}"
LOGIN_URL = f"http://127.0.0.1:8000/api/v1/login"
MOVE_URL = "http://127.0.0.1:8000/api/v1/move"
game_state = {}

async def login_request():
    """Simulates a frontend login."""
    
    payload = {"username": USERNAME}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(LOGIN_URL, json=payload)

    assert response.status_code == 200  # Ensure the request was successful

async def reset_request():
    """Reset Game state"""

    async with httpx.AsyncClient() as client:
        response = await client.get(RESET_URL)

    assert response.status_code == 200  # Ensure the request was successful
    game_state = response.json()
    assert game_state["current_position"] == [0, 0]

async def move_request(dir):
    """Simulates a frontend move request."""

    payload = {"username": USERNAME, "direction": dir}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(MOVE_URL, json=payload)

    assert response.status_code == 200  # Ensure the request was successful
    game_state = response.json()
    x, y = game_state["current_position"]
    if direction == "up" and y > 0:
        y -= 1
    elif direction == "down" and y < game_state["map_size"][1] - 1:
        y += 1
    elif direction == "left" and x > 0:
        x -= 1
    elif direction == "right" and x < game_state["map_size"][0] - 1:
        x += 1
        
    game_state["current_position"] = [x, y]


@pytest.mark.asyncio
async def test_integration():
    await login_request()
    #print(game_state)
    await reset_request()
    #print(game_state)
    for i in range(5):
        await move_request("down")
        #print(game_state)
    await move_request("right")
    assert game_state["current_position"] == [1,5]

@pytest.mark.asyncio
async def test_solver():
    await login_request()
    await reset_request()
    for i in range(5):
        await move_request("down")
    #print(game_state)
    assert game_state["health"] == 666
