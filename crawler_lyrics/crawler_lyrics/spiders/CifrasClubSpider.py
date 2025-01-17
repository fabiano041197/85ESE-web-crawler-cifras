# -*- coding: utf-8 -*-
import scrapy


class CifrasClubSpider(scrapy.Spider):
    name = 'Cifras-Club'
    allowed_domains = ['cifraclub.com.br']
    start_urls = ['https://www.cifraclub.com.br/catolicas/']

    def parse(self, response):
        music_elements = response.xpath('//li[@data-name]')
        domain_url = 'https://www.cifraclub.com.br'

        for music_element in music_elements:
            music_link = domain_url + music_element.css('a.art_music-link::attr(href)').get()

            yield response.follow(music_link, self.parse_lyrics)

    def parse_lyrics(self, response):
        link = response.url
        
