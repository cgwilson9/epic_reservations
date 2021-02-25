import requests
import json
import sys
import time
from pygame import mixer

def get_response(resort_name):
	pass

def main():
	available = False
	date = sys.argv[1]
	# resort = sys.argv[2]
	mixer.init()
	# load tunes
	mixer.music.load('mr_305.mp3')
	while available == False:
		response = requests.get("https://www.parkcitymountain.com/api/LiftAccessApi/GetLiftTicketControlReservationInventory?\
			startDate=02/24/2021&endDate=04/04/2021&_=1614190187185", 
			params={'startDate': '02/24/2021', 'endDate': '04/04/2021', '_': '1614190187185'},
			headers={'__requestverificationtoken': 'a-EhD96Q__we_PGJa2m1-t4KyyGWYvhyJJE7M2XpW07xeF2BAzm9EMqlNRjHa56Dml0rGZi6txOKPlnr7YBpbtMKkR01:2ocP1ZBe1pNt9-BViBSQs1vRtoFTOgTj0TSV3Exjt-qO6187Po7qfx925qTFpkmdNzyHfRqA0PJd0xh9d1Zpdjfp9w19yL1zdrMyEG8zJgC4HCUS0', 'cookie':'AKA_A2=A; QueueITAccepted-SDFrts345E-V3_vailresortsecomm1=EventId=vailresortsecomm1&QueueId=718d0318-d4e7-457a-8f9a-f9450d86017b&RedirectType=safetynet&IssueTime=1614188480&Hash=1d5d2d921dcae806f2da569d980032c29f078e9db418ac8494d2ab9ce667daca; ASP.NET_SessionId=h2mpeq0y12iwuc2uf5ilsq55; SC_ANALYTICS_GLOBAL_COOKIE=06443daea1214903b1221559fd4c04f1|False; __RequestVerificationToken=8pxBfbshsPi5kmIwHPip--_05L-Ju48DOiQMzvwi4YudK3MpD6_Ah1pSYxCmImGZYFhLWLo7zEBFkay-o9VK09Sal4E1; vr_product_reminder=true; rxVisitor=1614188481295DPFFBILP1LBEJIOMIHII4N03AFN7QKAO; AMCV_974C370453295F9A0A490D44@AdobeOrg=T; AMCVS_974C370453295F9A0A490D44@AdobeOrg=1; bm_mi=25A38DE8D8315B492AD5414685F9DE07~foL4LyC57D91BHy1EyjAty2VmnFjlr+LBSZVVrj4FCFZyJ9vJfkZQ3TGQncIQit/JsFHPEx+kIu+7gUHJyNI06kUEp3o+Yrtr368Tb9pLAU457QuqkuGP6In/t+QD1QQCdc7Ckgjc3ws9pdqhDpQN7StR+aEtoPnIamSjw6oSkSBtt8F/pkhcmwk8/X2ldTMJ3bqvpJn5FnFGLgDFIrYJ1zwjnVXczNFl6QoYvL1hblWcpGbikXLTuXA1RBToWTf/ARWf3QIP2KW29a6hEnsuA==; ak_bmsc=3AF83EAD3C7CE1FEE075B18A9D608D3D173CA8741E2A0000C08F36600B59FA11~plfCJhGrjxlHpGQbG1BaiJGxnXHsBniGeLnsBHxkLL00PT7ikaoAjIIHwMwtfcEdZ+RDHLuSD9U7+TyQF/fjmp3tDvHOU5aO+r71YsdcwYh5VIU/z89oRC9JPpdGbvGGXI1iQ/y4LduqfKmrNtyC7CfJuUfWkaMGRMNXlhAEypWG0QyTaWWCPeCWwPPv1SPC0v645bgQYIGWGlrr2olUFCgwkN/VUxv0wZvYfm1TAi9MNem4t8p57lkIiCzztgtYRf; check=true; dDweatherLastChecked=2021-02-24T10:41:25-07:00; s_vnum=1616780486380&vn=1; s_invisit=true; s_cc=true; s_lv_s=Less than 1 day; _fbp=fb.1.1614188486746.1449495174; rbuid=5600871949418525886; AAMC_vailresorts_0=REGION|9; aam_uuid=41454432050716519791177425327924319233; LPVID=FiM2Y1MDUxNmFiZThiMThi; LPSID-31842070=dNXNsPo5RgmV0CE2M726Mg; dtCookie=v_4_srv_2_sn_38CBD097B95C07B394FAC348409D5AEC_perc_100000_ol_0_mul_1_app-3A0d20c77a5fc281dd_0; TS0124474f=01d73c084b818b49e1c86e4f429db5be79184cef90504aedbd652a57da957886f5d6221a1543d4eb656e12213dd7dd40a94cbf2730; dDuserEmail=cgwilson94@gmail.com; .ASPXAUTH=E36C5A99A3E4F3EF066D59E28D7D6BFB19431969EDF537E57CBF730EBBB9E1E4DC73B1E33882BF2EA72A0E145819721465D358E3440E0A4475F7A4080A6DC3888CA0D38B7D84FB657A4385AC271AB31AEF3E53A5B4F70EDD32C050D87BA432CE7440CE27A418B2B94E1E349698BE80B5BAC26309E1A5D55B7995F9232F2E4502F4F2EFBF9751BB8E9A38542112CE09195F1BC26159998DB63795228DED113126E6AA2EDEC141F8E7C6CA47BF412A95977AB19BA1C8165FBE22A3C3CDEE303E0D1D198D80B98E92B76A4DDCE407C5472092398717222BED6AB41907A6A1C7AFED855D37C691E965D9FB19927E6C49D744041D761E07D4078A02E0DA1D331C39F6F13CA7DD9271FE6DC0F63C1C5F25A3CC25146E9FA143C3E9AA1775923DC23AA060E614145855D9BF30A6DFA5E2B22F6BB05F3EAC68413AC2C247796CA5B7EE73512A4F3035C24043EEC3C01A8CB73E2553A547F4; vr3_authenticated=45b1292a-d34a-4e1f-a26f-3c29bc918ef8; vr3_secure_auth=LcMx_7nhxLriBIV1Cgbc6g2=A2fdc95ipSlwI9I01LWlLg2&fKtZw7qa_sg1=OMROdzhWEENqd-h7EQVCoA2; dDrposID=12541714; OptanonAlertBoxClosed=2021-02-24T18:07:31.123Z; mbox=session#3ebe3fbcc0ef4f209e6400e41439b343#1614191978|PC#3ebe3fbcc0ef4f209e6400e41439b343.35_0#1677433287; gpv_pn=Park City:plan-your-trip:lift-access:Reservations; adcloud={"_les_v":"y,parkcitymountain.com,1614191918"}; QueueITAccepted-SDFrts345E-V3_epicpasspriority1203=EventId=epicpasspriority1203&QueueId=68b23f22-3cf5-46ef-b148-97100daa59bb&RedirectType=safetynet&IssueTime=1614190144&Hash=72c0afc60f7854bc1ede24e6ddf9df43a2c85d7acf4ab48fd0653c49e4eadf6f; s_sq=[[B]]; s_tp=3474; s_ppv=Park%20City%3Aplan-your-trip%3Alift-access%3ALift%20Tickets,29,29,1018; s_lv=1614190185363; s_nr=1614190185364-New; TS019b45a2=01d73c084ba20115d70278689f9c013773d8f33805b047a899c6b5c25fd793efb231edcd33f61ce055e9542f4a4a3960597f1cbbbb; TS01da35d0=01d73c084ba20115d70278689f9c013773d8f33805b047a899c6b5c25fd793efb231edcd33f61ce055e9542f4a4a3960597f1cbbbb; dtSa=-; dtLatC=4; rxvt=1614191987166|1614188481296; dtPC=2$190187151_889h1vAASDKJCBMHADIPMSAMMCKCMJAAVIUFFP-0e10; RT="z=1&dm=www.parkcitymountain.com&si=5ed4aa6c-e383-42ef-b934-e70629aea9c9&ss=kljq56qi&sl=4&tt=pq2&bcn=//34089f75.akstat.io/"; AMCV_974C370453295F9A0A490D44@AdobeOrg=1406116232|MCIDTS|18683|MCMID|40198742279086844852169023040969439823|MCAAMLH-1614794987|9|MCAAMB-1614794987|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1614197387s|NONE|MCAID|NONE|vVersion|2.5.0; OptanonConsent=isIABGlobal=false&datestamp=Wed+Feb+24+2021+11:09:47+GMT-0700+(Mountain+Standard+Time)&version=5.13.0&landingPath=NotLandingPage&groups=C0001:1,C0002:1,C0003:1,C0004:1&hosts=&AwaitingReconsent=false&geolocation=;; bm_sv=43768330A076C472BBB232C6157FBC2F~w1AqLG5F6wkvVLlts06nyVGdYeJF4xU8OSkQ6W3EW92nZzxddCbQa/xNiAUOXOS0eD2kS99OwFn044AqfftW3vyFkmg7IldXvTvmB+5GwDgxadxn1Vk0/XgiHzalHQt2SRjn7DAdSjwqZAuQHd8Qy67Nze8ULJJMwm18thvvGSA='})
		json_response = response.json()
		for elem in json_response:
			if elem['InventoryDate'] == date:
				if elem['Remaining'] > 0:
					print("Available!!!")
					mixer.music.play()
					time.sleep(30)
					available = True
				elif elem['Remaining'] == 0:
					print("Unavailable")
				else:
					print("Not sure lol.")
		# does Epic rate limit haha
		time.sleep(5)

if __name__ == "__main__":
    main()