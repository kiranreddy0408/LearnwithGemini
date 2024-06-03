import asyncio
from gemini_webapi import GeminiClient

# Replace "COOKIE VALUE HERE" with your actual cookie values.
# Leave Secure_1PSIDTS empty if it's not available for your account.
Secure_1PSID = "g.a000jQg2wXGmrAorzR5pvjkiYFeiIEhsYZ_9eD1WcaWs7kSzbOxLrmdXJBq8whjuF2anfRYBiAACgYKARISAQASFQHGX2Mi45oMOZkQo6NiMBubbBfzzRoVAUF8yKomzYaft3ji-psUYzSKGSjg0076"
Secure_1PSIDTS = "sidts-CjEBLwcBXGy819IdNri774oFl8xE8zUYVNdeggdmmPvlxizWBhcD7QpdQivoeFl3XiviEAA"


async def main():
    # Initialize the GeminiClient with the given cookies
    client = GeminiClient(Secure_1PSID, Secure_1PSIDTS, proxies=None)
    
    # Initialize the client with auto_refresh enabled and a timeout of 30 seconds
    await client.init(timeout=30, auto_close=False, close_delay=300, auto_refresh=True)
    
    # Generate content based on a prompt
    # prompt = "explain this topic 'hybridization of sp2 orbitals' with an explanation and online resources and a example image link if any possible. give all content in this json object format:{'explanation':explanation,'resource-links':['link1','link2'],'image-link':link}"
    response = await client.generate_content("explain this topic 'hybridization of sp2 orbitals' with an explanation and online resources and a example image link if any possible. give all content in this json object format:{'explanation':explanation,'resource-links':links,'youtube-links':links,'image-link':link}")
    # response = await client.generate_content("Examples of sp2 hybridization")
    for image in response.images:
        print(image, "\n\n----------------------------------\n")
    # Print the generated response text
    print(response)

# Run the main function
asyncio.run(main())