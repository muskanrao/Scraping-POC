import requests
import pandas as pd
import json




'''
url = "https://www.skyscanner.co.in/g/conductor/v1/fps3/search/?geo_schema=skyscanner&carrier_schema=skyscanner&response_include=query%3Bdeeplink%3Bsegment%3Bstats%3Bfqs%3Bpqs"

payload = json.dumps({
  "market": "IN",
  "locale": "en-GB",
  "currency": "INR",
  "alternativeOrigins": False,
  "alternativeDestinations": False,
  "destination": {
    "entityId": "95673361",
    "id": "MAA",
    "airportId": "MAA",
    "name": "Chennai",
    "cityId": "IMAA",
    "cityName": "Chennai",
    "geoContainerId": "32575954",
    "countryId": "IN",
    "type": "Airport",
    "centroidCoordinates": [
      80.176944,
      12.993333
    ],
    "rawLocationId": "maa"
  },
  "adults": 1,
  "cabin_class": "economy",
  "child_ages": [],
  "options": {
    "include_unpriced_itineraries": True,
    "include_mixed_booking_options": True
  },
  "origin": {
    "entityId": "95673498",
    "id": "DEL",
    "airportId": "DEL",
    "name": "Indira Gandhi International ",
    "cityId": "IDEL",
    "cityName": "New Delhi",
    "geoContainerId": "27540706",
    "countryId": "IN",
    "type": "Airport",
    "centroidCoordinates": [
      77.100833,
      28.573611
    ],
    "rawLocationId": "del"
  },
  "outboundDate": "2024-02-02",
  "prefer_directs": False,
  "state": {},
  "viewId": "506285d5-1cad-4721-a3a5-65aaec3b1dad",
  "travellerContextId": "9b4d0773-b932-48bc-a4a2-8433091682a1",
  "trusted_funnel_search_guid": "506285d5-1cad-4721-a3a5-65aaec3b1dad",
  "legs": [
    {
      "origin": "DEL",
      "originEntityId": "95673498",
      "destination": "MAA",
      "destinationEntityId": "95673361",
      "date": "2024-02-02",
      "add_alternative_origins": False,
      "add_alternative_destinations": False
    }
  ]
})
headers = {
  'authority': 'www.skyscanner.co.in',
  'accept': 'application/json',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': 'traveller_context=9b4d0773-b932-48bc-a4a2-8433091682a1; __Secure-anon_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImM3ZGZlYjI2LTlmZjUtNDY4OC1iYjc3LWRiNTY2NWUyNjFkZSJ9.eyJhenAiOiIyNWM3MGZmZDAwN2JkOGQzODM3NyIsImh0dHBzOi8vc2t5c2Nhbm5lci5uZXQvbG9naW5UeXBlIjoiYW5vbnltb3VzIiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC91dGlkIjoiOWI0ZDA3NzMtYjkzMi00OGJjLWE0YTItODQzMzA5MTY4MmExIiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC9jc3JmIjoiYjdiMTZlMDg0NDFjMmY4YjI1YzQ3MWFjMzI3ZWRkNzEiLCJodHRwczovL3NreXNjYW5uZXIubmV0L2p0aSI6IjE0MzVmMmY5LTFiMzYtNDQ2ZS1iZWQwLTc4NDRiMDJkMzNmNCIsImlhdCI6MTcwNjcxNTA0NCwiZXhwIjoxNzY5Nzg3MDQ0LCJhdWQiOiJodHRwczovL2dhdGV3YXkuc2t5c2Nhbm5lci5uZXQvaWRlbnRpdHkiLCJpc3MiOiJodHRwczovL3d3dy5za3lzY2FubmVyLm5ldC9zdHRjL2lkZW50aXR5L2p3a3MvcHJvZC8ifQ.je1Sze9d3xNTRFNllMFTN8HAWewNvLtNb7VYR-JOJSAVxkNlc2CqppV2QuiIdHWRChTxkPMv3GOOO8M57igjjaUxvVbXT2AQm4hMeM--Aq-KFgBW6OxnooOT0UkZUFeOIaMVREMciDkgKLoNYVrprqGl0Qxi5PP4ckzaSw0fuKUKeDO1yz5hhxVQTHQ_02eemTfcVX0MpOVq3mH7jHxwRO1Go8Vhwj0BDseePbMqH7vVLGe4VqZsHKTPGdD9VZf5VaBc9EZryyE6PomTlafOKXJ9sN0C0ZiuoXdQvZT9dmpnHDBkUiPR0yONrNuIUP8weT2CCTRmIp_VD9YJ0Fug8A; __Secure-anon_csrf_token=b7b16e08441c2f8b25c471ac327edd71; ssculture=locale:::en-GB&market:::IN&currency:::INR; __Secure-ska=b6d59833-c239-4381-851e-6b131e386e53; device_guid=b6d59833-c239-4381-851e-6b131e386e53; pxcts=b43112a7-c04d-11ee-87b7-638f3951ea96; _pxvid=b331b682-c04d-11ee-9301-5815895560ed; _gcl_au=1.1.635012943.1706715047; preferences=9b4d0773b93248bca4a28433091682a1; _gid=GA1.3.1884241002.1706715086; __gsas=ID=ec2a4dddf317d158:T=1706715086:RT=1706715086:S=ALNI_MaxswhrUuyHvrOClLaXcgzmqWu7Zw; QSI_S_ZN_8fcHUNchqVNRM4S=v:0:0; _fbp=fb.2.1706715090927.816970579; _clck=1rfesiw%7C2%7Cfiw%7C0%7C1491; _pxhd=n-lHtbbytGBiDtWGiFZRFhwz5uqdMK/GIWFdtUPUSQ/JKzA21HpYRvkdmf/aAkogKfzjcBxi47SyeNN10mJfOA==:SzMZjgPeuUTUqNKERyP64--QIKdDhDnTPxFgUqJa/cSgdrZh0bOUdwbaB3SPUYThdpVlye3jneDDQDXFlWx0RiRtW8jH-RIV45lLOVt-xh4=; ssaboverrides=; abgroup=16204834; _uetsid=ce621a90c04d11ee8da9156939572a57; _uetvid=ce621940c04d11eea88ff3e684237ea8; _clsk=rwii77%7C1706806647138%7C2%7C0%7Cu.clarity.ms%2Fcollect; __gads=ID=2eb7844542ef225c:T=1706715087:RT=1706806646:S=ALNI_MbrhkL3K17ZS6fe5mPsoydARhvvag; __gpi=UID=00000cf53e8946c6:T=1706715087:RT=1706806646:S=ALNI_Mbt1Z9jUfLWjf940ziQDt1bRDvdWg; __eoi=ID=e122739684a65445:T=1706715087:RT=1706806646:S=AA-AfjZuQpX7xZuFN2TD-AWbSe72; ssab=Autosuggest_Flight_NearbyAirport_V4:::b&BD_Save_To_List_Hotels_Enabled_V6:::b&BD_enable_deals_colors_experiment_V1:::a&Car_Hire_Peak_Desktop_GraphicPromo_V3:::a&Car_Hire_Peak_Desktop_GraphicPromo_IL_AE_V1:::a&EnableAcornGtmIntegration_V5:::b&EnableMonthViewGtmIntegration_V4:::b&EnableSimplifiedGrpcClientWrapper_V3:::a&Enable_USP_Messaging_V3:::b&Flexible_Search_Direct_Days_Banana_V3:::b&LivePricingPOC_V17:::a&MAT_supplier_rating_varianta_on_desktop_V6:::b&Merch_AirCanada_GP_Desktop_V1:::b&Merch_AirCanada_NDE_Desktop_V1:::a&Multi_city_search_Nav_Card_on_Desktop_V3:::a&autosuggest_hotel_recall_intention_optimize_V2:::a&banana_internal_linking_gc_V8:::a&combined_explore_filter_direct_pill_web_V3:::b&dayview_stops_filter_persistence_V1:::a&fps_lus_aqs_holdout_set_web_V1:::a&fps_mr_fqs_flights_ranking_mimir_v2__25i_desktop2_V0:::c&fps_ttlr_early_timeout_banana_V83:::a&fps_ttlr_early_timeout_web_V21:::a&hotels_xsell_format_V2:::a&sam_split_test_0843b6ee97171895_V0:::a&sam_split_test_0e7d97febb2de144_V0:::a&sam_split_test_1caa55bf01e67a61_V0:::a&sam_split_test_a9b7083b54fb9123_V0:::a&sam_split_test_fe8482441887800b_V0:::a&terra_proxy_get_v2_entities_V4:::a&terra_proxy_suggested_airports_V42:::a&without_randomization_V2:::b; experiment_allocation_id=55f16cb47c89aca25d2f2f510a5cbfafbf22f466a142f7f46be02a3b5da5c9ab; avoid_banana_results=true; scanner=currency:::INR&legs:::DEL|2024-02-02|MAA&tripType:::one-way&rtn:::false&preferDirects:::false&outboundAlts:::false&inboundAlts:::false&oym:::2402&oday:::02&wy:::0&cabinclass:::Economy&adults:::1&adultsV2:::1&children:::0&childrenV2&infants:::0&iym:::2402&iday:::07&from:::DEL&to:::MAA; QSI_S_ZN_0VDsL2Wl8ZAlxlA=r:5:3; _px3=c2f77a79f620bd6549670407db7ad317816fe1cd13785ecb408a1812f939a8a2:ZmHYT6If3r+rb21zhgWV6/Bg/GWaSZwaUMpA3mecaftFjErHGSLKp48QDBttK2L7dc5LlzOsHNUAZVqxwCbvvg==:1000:fzSyUExWpYZ6+5eMCYjp5h4HnlkBViKY8BHgwaW9JtWYNGxnK9OEASdltGhVNqKhYZ15QfTU5LBlPOiytOyAs5VNO6+bPpYnZANYZ+984t80Rb1dVtfjSz+rHBpiC925+yeEqek4RCE+V1NX7yXn41lH3D9CkE9Z6VEqucEiAECYDy/XUiM7+66UqC0CreHMz2Z/r2XWPxGeAXILsbYaqN4T1vqyXt1alqzk3kF86oU=; cto_bundle=npVH519nR201QWQ2UHJ2TUhOQmwwSDVyR2Z5QVdkQTJpNUJqdThONkJvQW1nQ3FvdGtHMHBzQkN6ZWVaMjJIQkFCNlpCNTNBUGtEYjFVOWd1dFVMc0hpaVBxbWJzOEEwTEhEMWpPY1NxdkVHcUhkck5tQklFT2hpSktWRHhiJTJCbk1iJTJCcGhTTGFkRmt3azlqV2lmZFhnUTVmVUJvcnJ0U3htSmMyRHZsbkIlMkI2SkpTdUlkQjVxSVdWa2xvJTJGemxQVko0ZEElMkZhZjNrZGFER0U2SUkwOWxxRXBzN1BEeTJJV2c5UWJVaWQ3YW1Odzl1ZkU0YTk5UUxuam1qTmtWVkdKeUlQVEZzRmhWSW92MTA2VmllSTdKejd1ZyUyQjk1dyUzRCUzRA; _ga_3TVCQ3LJNW=GS1.1.1706806644.6.1.1706806732.0.0.0; _ga=GA1.3.b6d59833-c239-4381-851e-6b131e386e53.1706715046; _gat=1; _pxhd=39-wHIr6SaqNdpMGadcRBYevSQSOuwq/Lz7ddeHsy--jnuJHsGSyH2sqjik8HP13PnY6Bms/Xq88EXJYS5hjcA==:2UrjjJ0BYEq5rxUUdE4kvj3RKZqOZ-lYXLtUk8rIBScdcZq-20rxnsxWQiCv9dhg2y90wOrYUt4be2FW3M3Tn9KzaauZ-S5PayD4AmpsFo8=',
  'origin': 'https://www.skyscanner.co.in',
  'pragma': 'no-cache',
  'referer': 'https://www.skyscanner.co.in/transport/flights/del/maa/240202/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=0',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-skyscanner-channelid': 'website',
  'x-skyscanner-devicedetection-ismobile': 'false',
  'x-skyscanner-devicedetection-istablet': 'false',
  'x-skyscanner-traveller-context': '9b4d0773-b932-48bc-a4a2-8433091682a1',
  'x-skyscanner-utid': '9b4d0773-b932-48bc-a4a2-8433091682a1',
  'x-skyscanner-viewid': '506285d5-1cad-4721-a3a5-65aaec3b1dad'
}

#response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
'''

'''
url = "https://www.skyscanner.co.in/g/conductor/v1/fps3/search/323a60c9-0e7d-4a4e-b426-908fd64bdbac?geo_schema=skyscanner&carrier_schema=skyscanner&response_include=query%3Bdeeplink%3Bsegment%3Bstats%3Bfqs%3Bpqs"

payload = {}
res=[]
headers = {
  'authority': 'www.skyscanner.co.in',
  'accept': 'application/json',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': 'traveller_context=9b4d0773-b932-48bc-a4a2-8433091682a1; __Secure-anon_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImM3ZGZlYjI2LTlmZjUtNDY4OC1iYjc3LWRiNTY2NWUyNjFkZSJ9.eyJhenAiOiIyNWM3MGZmZDAwN2JkOGQzODM3NyIsImh0dHBzOi8vc2t5c2Nhbm5lci5uZXQvbG9naW5UeXBlIjoiYW5vbnltb3VzIiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC91dGlkIjoiOWI0ZDA3NzMtYjkzMi00OGJjLWE0YTItODQzMzA5MTY4MmExIiwiaHR0cHM6Ly9za3lzY2FubmVyLm5ldC9jc3JmIjoiYjdiMTZlMDg0NDFjMmY4YjI1YzQ3MWFjMzI3ZWRkNzEiLCJodHRwczovL3NreXNjYW5uZXIubmV0L2p0aSI6IjE0MzVmMmY5LTFiMzYtNDQ2ZS1iZWQwLTc4NDRiMDJkMzNmNCIsImlhdCI6MTcwNjcxNTA0NCwiZXhwIjoxNzY5Nzg3MDQ0LCJhdWQiOiJodHRwczovL2dhdGV3YXkuc2t5c2Nhbm5lci5uZXQvaWRlbnRpdHkiLCJpc3MiOiJodHRwczovL3d3dy5za3lzY2FubmVyLm5ldC9zdHRjL2lkZW50aXR5L2p3a3MvcHJvZC8ifQ.je1Sze9d3xNTRFNllMFTN8HAWewNvLtNb7VYR-JOJSAVxkNlc2CqppV2QuiIdHWRChTxkPMv3GOOO8M57igjjaUxvVbXT2AQm4hMeM--Aq-KFgBW6OxnooOT0UkZUFeOIaMVREMciDkgKLoNYVrprqGl0Qxi5PP4ckzaSw0fuKUKeDO1yz5hhxVQTHQ_02eemTfcVX0MpOVq3mH7jHxwRO1Go8Vhwj0BDseePbMqH7vVLGe4VqZsHKTPGdD9VZf5VaBc9EZryyE6PomTlafOKXJ9sN0C0ZiuoXdQvZT9dmpnHDBkUiPR0yONrNuIUP8weT2CCTRmIp_VD9YJ0Fug8A; __Secure-anon_csrf_token=b7b16e08441c2f8b25c471ac327edd71; ssculture=locale:::en-GB&market:::IN&currency:::INR; ssaboverrides=; abgroup=35282582; __Secure-ska=b6d59833-c239-4381-851e-6b131e386e53; device_guid=b6d59833-c239-4381-851e-6b131e386e53; pxcts=b43112a7-c04d-11ee-87b7-638f3951ea96; _pxvid=b331b682-c04d-11ee-9301-5815895560ed; _gcl_au=1.1.635012943.1706715047; ssab=Autosuggest_Flight_NearbyAirport_V4:::b&BD_Save_To_List_Hotels_Enabled_V6:::b&BD_enable_deals_colors_experiment_V1:::a&Car_Hire_Peak_Desktop_GraphicPromo_V3:::a&Car_Hire_Peak_Desktop_GraphicPromo_IL_AE_V1:::a&EnableAcornGtmIntegration_V5:::b&EnableMonthViewGtmIntegration_V3:::b&EnableSimplifiedGrpcClientWrapper_V3:::a&Enable_USP_Messaging_V3:::b&Flexible_Search_Direct_Days_Banana_V3:::b&LivePricingPOC_V17:::a&MAT_supplier_rating_varianta_on_desktop_V6:::b&Merch_AirCanada_GP_Desktop_V1:::b&Merch_AirCanada_NDE_Desktop_V1:::a&Multi_city_search_Nav_Card_on_Desktop_V3:::a&banana_internal_linking_gc_V8:::a&combined_explore_filter_direct_pill_web_V2:::b&dayview_stops_filter_persistence_V1:::a&dummy_jekyll2_V5:::a&fps_mr_fqs_flights_ranking_mimir_v2__25i_desktop2_V0:::c&fps_ttlr_early_timeout_banana_V83:::a&fps_ttlr_early_timeout_web_V21:::a&hotels_xsell_format_V2:::a&sam_split_test_0843b6ee97171895_V0:::a&sam_split_test_0e7d97febb2de144_V0:::a&sam_split_test_1caa55bf01e67a61_V0:::a&sam_split_test_a9b7083b54fb9123_V0:::a&sam_split_test_fe8482441887800b_V0:::a&terra_proxy_get_v2_entities_V4:::a&terra_proxy_suggested_airports_V42:::a&without_randomization_V2:::b; experiment_allocation_id=b565d5ac9ae7d458609e3d710e7eeeeeeb5655796c959f82075251e81cf138c4; preferences=9b4d0773b93248bca4a28433091682a1; _gid=GA1.3.1884241002.1706715086; __gsas=ID=ec2a4dddf317d158:T=1706715086:RT=1706715086:S=ALNI_MaxswhrUuyHvrOClLaXcgzmqWu7Zw; QSI_S_ZN_8fcHUNchqVNRM4S=v:0:0; _fbp=fb.2.1706715090927.816970579; _clck=1rfesiw%7C2%7Cfiv%7C0%7C1491; QSI_S_ZN_0VDsL2Wl8ZAlxlA=r:5:2; _pxhd=2eUlvG8ZRKZR/x9bm8zrr1FPdOlChpk/q0Ac--ZD32rTtDuxR3zaXdbU-1qLq8NYr-38FywIHwgJ64EuKXF52Q==:clbeAi7XLChx8/SqYWK5CIW-HfFlw/9MaGhlgsfqxGZJ/K4a5IfPUaPGYIfRrIvDqJp2OGv/pXkTxpz3Bjj2CLBQZd5mhp87CcQqJookLfI=; __gads=ID=2eb7844542ef225c:T=1706715087:RT=1706722946:S=ALNI_MbrhkL3K17ZS6fe5mPsoydARhvvag; __gpi=UID=00000cf53e8946c6:T=1706715087:RT=1706722946:S=ALNI_Mbt1Z9jUfLWjf940ziQDt1bRDvdWg; __eoi=ID=e122739684a65445:T=1706715087:RT=1706722946:S=AA-AfjZuQpX7xZuFN2TD-AWbSe72; avoid_banana_results=true; scanner=currency:::INR&legs:::DEL|2024-02-02|MAA|||&tripType:::one-way&rtn&preferDirects:::false&outboundAlts&inboundAlts&oym:::2402&oday:::02&wy:::0&cabinclass:::Economy&adults:::1&adultsV2:::1&children:::0&childrenV2&infants:::0&iym:::2402&iday:::07&from:::DEL&to:::MAA; _gat=1; _ga=GA1.1.b6d59833-c239-4381-851e-6b131e386e53.1706715046; _ga_3TVCQ3LJNW=GS1.1.1706723058.3.1.1706723127.0.0.0; cto_bundle=8GXRkl9nR201QWQ2UHJ2TUhOQmwwSDVyR2Z3SHpoUWd1aUR6UkdqQTdvemFlJTJGNm9CTjhGYU1jbU5UQVNVSFViajJScWczUjlYcDI1UjBTV1clMkYyblFrd2cwaXlmTVFsVzdBM210Ym5SJTJGUkVhR3BuRUhZck53UnNrY0hqJTJGQlR3VGRiMG1SdDRHa2NtWGJ5TG51YVJwWU9pQ0NxbTFZRklOaWUlMkZ1NHlsSTN1TVFUdmg0R21YRGRxalBxcHcyR3piZ2hJV0FuSmRNOTFtNUxKeTVpUTdhNWM2dGtNV3klMkJsSHdFT1UlMkJGRlA1cVc2c2pZQiUyRmlNclI3T2Z3OFhVUGFyUGNpSUpscVRBekFEaVFwVWtnZjNkcCUyQm15MHo0N2p4cHV1NTBhaFdnVHd0UmdQUFluWGpLWDN4anRIVHgzcXlFMjJWViUyRlQlMkI; _uetsid=ce621a90c04d11ee8da9156939572a57; _uetvid=ce621940c04d11eea88ff3e684237ea8; _px3=09d8a5f9ebb05917df1a26dabbac191c289da1be6335498cda49efb67cef8068:iFTQgDD8aGN6QQG8iBkZyV2tR73VKyqRIvX8pxPk9L90+9TsBd8eaxSQbjDhhEo12kDp6h64dlRdMJc3BXBsBQ==:1000:djZxlwkfj7NkgfGcUFQ5lFGhDas805O0uZS4pgxjOO/YcVmKF6bloPM8uuhqdsne4KQQDOjbV0DsrPdgB3XxmIE61mpxYRX9AgriaQwYuMg/wedeIA1qFo3uzEmkoLh8ATpuyLUceG3upRwj5F3Qg/cb3p+wCZwSpYr8IoNpOkPKTbykD6lVIuBTC6AQX4ohvZPCzAa9NJgflKo2PPZO8uEBgrlUiUwPmKPpymlEQy0=; _clsk=1dhk3y3%7C1706723130281%7C8%7C0%7Cq.clarity.ms%2Fcollect; _pxhd=39-wHIr6SaqNdpMGadcRBYevSQSOuwq/Lz7ddeHsy--jnuJHsGSyH2sqjik8HP13PnY6Bms/Xq88EXJYS5hjcA==:2UrjjJ0BYEq5rxUUdE4kvj3RKZqOZ-lYXLtUk8rIBScdcZq-20rxnsxWQiCv9dhg2y90wOrYUt4be2FW3M3Tn9KzaauZ-S5PayD4AmpsFo8=',
  'pragma': 'no-cache',
  'referer': 'https://www.skyscanner.co.in/transport/flights/del/maa/240202/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=0',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-gateway-servedby': 'gw52.skyscanner.net',
  'x-skyscanner-channelid': 'website',
  'x-skyscanner-devicedetection-ismobile': 'false',
  'x-skyscanner-devicedetection-istablet': 'false',
  'x-skyscanner-traveller-context': '9b4d0773-b932-48bc-a4a2-8433091682a1',
  'x-skyscanner-utid': '9b4d0773-b932-48bc-a4a2-8433091682a1',
  'x-skyscanner-viewid': '69eeaea8-b40c-41fc-b1c3-16e8aa07133d'
}
res = []
#esponse = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
data = response.json()  # Extracting JSON data from response

'''



#using json :
with open('a.json', 'r') as file:
    json_data = file.read()
    data = json.loads(json_data)

# Extracting leg_ids 
leg_ids_array = []
for itinerary in data['itineraries']:
    leg_ids_array.extend(itinerary['leg_ids'])

# Printing the array of leg_ids
print("Leg IDs Array:")
print(leg_ids_array)


# Iterating through the json
# list
'''res= []

for itinerary in data['itineraries']:
    for pricing_option in itinerary['pricing_options']:
        price_amount = pricing_option['price'].get('amount')
        if price_amount is not None:
            res.append(price_amount)

print(res)'''

#df = pd.json_normalize(res)
#df.to_csv('firsyresults.csv')

#print(response.json())
