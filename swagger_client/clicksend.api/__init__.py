from __future__ import absolute_import

# flake8: noqa

# import apis into api package
from clicksend.api.account_api import AccountApi
from clicksend.api.account_recharge_api import AccountRechargeApi
from clicksend.api.contact_api import ContactApi
from clicksend.api.contact_list_api import ContactListApi
from clicksend.api.countries_api import CountriesApi
from clicksend.api.delivery_issues_api import DeliveryIssuesApi
from clicksend.api.detect_address_api import DetectAddressApi
from clicksend.api.email_delivery_receipt_rules_api import EmailDeliveryReceiptRulesApi
from clicksend.api.email_marketing_api import EmailMarketingApi
from clicksend.api.email_to_sms_api import EmailToSmsApi
from clicksend.api.fax_delivery_receipt_rules_api import FAXDeliveryReceiptRulesApi
from clicksend.api.fax_api import FaxApi
from clicksend.api.inbound_fax_rules_api import InboundFAXRulesApi
from clicksend.api.inbound_sms_rules_api import InboundSMSRulesApi
from clicksend.api.mms_api import MMSApi
from clicksend.api.master_email_templates_api import MasterEmailTemplatesApi
from clicksend.api.mms_campaign_api import MmsCampaignApi
from clicksend.api.number_api import NumberApi
from clicksend.api.post_direct_mail_api import PostDirectMailApi
from clicksend.api.post_letter_api import PostLetterApi
from clicksend.api.post_postcard_api import PostPostcardApi
from clicksend.api.post_return_address_api import PostReturnAddressApi
from clicksend.api.referral_account_api import ReferralAccountApi
from clicksend.api.reseller_account_api import ResellerAccountApi
from clicksend.api.sms_api import SMSApi
from clicksend.api.sms_delivery_receipt_rules_api import SMSDeliveryReceiptRulesApi
from clicksend.api.search_api import SearchApi
from clicksend.api.sms_campaign_api import SmsCampaignApi
from clicksend.api.statistics_api import StatisticsApi
from clicksend.api.subaccount_api import SubaccountApi
from clicksend.api.timezones_api import TimezonesApi
from clicksend.api.transactional_email_api import TransactionalEmailApi
from clicksend.api.transfer_credit_api import TransferCreditApi
from clicksend.api.upload_api import UploadApi
from clicksend.api.user_email_templates_api import UserEmailTemplatesApi
from clicksend.api.voice_api import VoiceApi
from clicksend.api.voice_delivery_receipt_rules_api import VoiceDeliveryReceiptRulesApi
