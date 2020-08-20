# youtube-researches

Just run:

`
docker-compose up
`

API is running in the 12345 port

Example request:

URL: <http://localhost:12345/researchs> POST

`
{
    "term": "cat",
    "days": [
        15,
        120,
        30,
        150,
        20,
        40,
        90
    ]
}
`
