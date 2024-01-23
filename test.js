const puppeteer = require('puppeteer');
const fs = require('fs');

(async() => {
    const url = process.argv[2];
    const browser = await puppeteer.launch();
    // use tor
    //const browser = await puppeteer.launch({args:['--proxy-server=socks5://127.0.0.1:9050']});
    const page = await browser.newPage();
    await page.setRequestInterception(true)
    page.setViewport({ width: 1024, height: 926 });

    // page.on('request', (request) => {
    //     console.log(`Intercepting: ${request.method} ${request.url}`);
    //     request.continue();
    // });
    await page.goto(url, { waitUntil: ['networkidle0', "domcontentloaded", "load"] });

    const title = await page.title();
    console.log(title);
    await page.screenshot({ path: 'example.png', full_page: true });
    const html = await page.content();

    await page.pdf({ path: 'example.pdf' })
        //console.log(html);
    fs.writeFileSync('page.html', html);

    browser.close();
})();