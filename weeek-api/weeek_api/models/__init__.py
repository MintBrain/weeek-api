"""Contains all the data models used in inputs/outputs"""

from .address_response import AddressResponse
from .api_response import ApiResponse
from .attachment import Attachment
from .attachment_service_enum import AttachmentServiceEnum
from .board import Board
from .board_column import BoardColumn
from .contact import Contact
from .contact_email import ContactEmail
from .contact_phone import ContactPhone
from .crm_contact import CrmContact
from .crm_contact_1 import CrmContact1
from .crm_contacts import CrmContacts
from .crm_currencies import CrmCurrencies
from .crm_deal import CrmDeal
from .crm_deal_attach_task_response_200 import CrmDealAttachTaskResponse200
from .crm_deals import CrmDeals
from .crm_funnel import CrmFunnel
from .crm_funnel_status import CrmFunnelStatus
from .crm_funnel_statuses import CrmFunnelStatuses
from .crm_funnels import CrmFunnels
from .crm_move_attached_deal_task_body import CrmMoveAttachedDealTaskBody
from .crm_move_deal_body import CrmMoveDealBody
from .crm_organization import CrmOrganization
from .crm_organization_1 import CrmOrganization1
from .crm_organizations import CrmOrganizations
from .crm_update_deal_funnel_body import CrmUpdateDealFunnelBody
from .crm_update_deal_status_body import CrmUpdateDealStatusBody
from .currency import Currency
from .current_user import CurrentUser
from .custom_field import CustomField
from .custom_field_config_type_0 import CustomFieldConfigType0
from .custom_field_config_type_0_type import CustomFieldConfigType0Type
from .custom_field_create_body import CustomFieldCreateBody
from .custom_field_create_body_config_type_0 import CustomFieldCreateBodyConfigType0
from .custom_field_create_body_config_type_0_type import CustomFieldCreateBodyConfigType0Type
from .custom_field_create_body_type import CustomFieldCreateBodyType
from .custom_field_option import CustomFieldOption
from .custom_field_option_1 import CustomFieldOption1
from .custom_field_option_1_color import CustomFieldOption1Color
from .custom_field_option_color import CustomFieldOptionColor
from .custom_field_type import CustomFieldType
from .custom_field_update_body import CustomFieldUpdateBody
from .custom_field_update_body_config_type_0 import CustomFieldUpdateBodyConfigType0
from .custom_field_update_body_config_type_0_type import CustomFieldUpdateBodyConfigType0Type
from .custom_field_value import CustomFieldValue
from .custom_field_value_config_type_0 import CustomFieldValueConfigType0
from .custom_field_value_config_type_0_type import CustomFieldValueConfigType0Type
from .custom_field_value_type import CustomFieldValueType
from .custom_field_values import CustomFieldValues
from .deal import Deal
from .deal_create_request import DealCreateRequest
from .deal_create_request_win_status import DealCreateRequestWinStatus
from .deal_update_request import DealUpdateRequest
from .deal_update_request_win_status import DealUpdateRequestWinStatus
from .deal_win_status import DealWinStatus
from .delete_crm_contacts_contact_id_tags_body import DeleteCrmContactsContactIdTagsBody
from .delete_crm_deals_deal_id_assignees_body import DeleteCrmDealsDealIdAssigneesBody
from .delete_crm_deals_deal_id_contacts_body import DeleteCrmDealsDealIdContactsBody
from .delete_crm_deals_deal_id_organizations_body import DeleteCrmDealsDealIdOrganizationsBody
from .delete_crm_deals_deal_id_tags_body import DeleteCrmDealsDealIdTagsBody
from .delete_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_response_200 import (
    DeleteCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdResponse200,
)
from .delete_crm_funnels_funnel_id_custom_fields_id_response_200 import (
    DeleteCrmFunnelsFunnelIdCustomFieldsIdResponse200,
)
from .delete_crm_organizations_organization_id_contacts_body import DeleteCrmOrganizationsOrganizationIdContactsBody
from .delete_crm_organizations_organization_id_tags_body import DeleteCrmOrganizationsOrganizationIdTagsBody
from .delete_tm_board_columns_id_response_200 import DeleteTmBoardColumnsIdResponse200
from .delete_tm_boards_id_response_200 import DeleteTmBoardsIdResponse200
from .delete_tm_projects_id_response_200 import DeleteTmProjectsIdResponse200
from .delete_tm_projects_project_id_custom_fields_custom_field_id_options_id_response_200 import (
    DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200,
)
from .delete_tm_projects_project_id_custom_fields_id_response_200 import (
    DeleteTmProjectsProjectIdCustomFieldsIdResponse200,
)
from .delete_tm_tasks_id_response_200 import DeleteTmTasksIdResponse200
from .delete_tm_tasks_task_id_time_entries_time_entry_id_response_200 import (
    DeleteTmTasksTaskIdTimeEntriesTimeEntryIdResponse200,
)
from .delete_tm_tasks_task_id_watchers_response_200 import DeleteTmTasksTaskIdWatchersResponse200
from .delete_ws_tags_2_response_200 import DeleteWsTags2Response200
from .email_response import EmailResponse
from .email_response_1 import EmailResponse1
from .funnel import Funnel
from .funnel_manage_request import FunnelManageRequest
from .funnel_status import FunnelStatus
from .funnel_status_manage_request import FunnelStatusManageRequest
from .get_attachments_attachment_id_response_200 import GetAttachmentsAttachmentIdResponse200
from .get_tm_board_columns_response_200 import GetTmBoardColumnsResponse200
from .get_tm_boards_response_200 import GetTmBoardsResponse200
from .get_tm_projects_id_response_200 import GetTmProjectsIdResponse200
from .get_tm_projects_response_200 import GetTmProjectsResponse200
from .get_tm_tasks_id_response_200 import GetTmTasksIdResponse200
from .get_tm_tasks_response_200 import GetTmTasksResponse200
from .get_user_me_response_200 import GetUserMeResponse200
from .get_ws_members_response_200 import GetWsMembersResponse200
from .get_ws_response_200 import GetWsResponse200
from .get_ws_tags_id_response_200 import GetWsTagsIdResponse200
from .get_ws_tags_response_200 import GetWsTagsResponse200
from .organization import Organization
from .organization_address import OrganizationAddress
from .organization_email import OrganizationEmail
from .organization_phone import OrganizationPhone
from .phone_response import PhoneResponse
from .phone_response_1 import PhoneResponse1
from .post_crm_contacts_contact_id_emails_body import PostCrmContactsContactIdEmailsBody
from .post_crm_contacts_contact_id_tags_body import PostCrmContactsContactIdTagsBody
from .post_crm_contacts_contacts_id_phones_body import PostCrmContactsContactsIdPhonesBody
from .post_crm_deals_deal_id_assignees_body import PostCrmDealsDealIdAssigneesBody
from .post_crm_deals_deal_id_attachments_body import PostCrmDealsDealIdAttachmentsBody
from .post_crm_deals_deal_id_attachments_response_200 import PostCrmDealsDealIdAttachmentsResponse200
from .post_crm_deals_deal_id_contacts_body import PostCrmDealsDealIdContactsBody
from .post_crm_deals_deal_id_organizations_body import PostCrmDealsDealIdOrganizationsBody
from .post_crm_deals_deal_id_tags_body import PostCrmDealsDealIdTagsBody
from .post_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_move_body import (
    PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
)
from .post_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_move_response_200 import (
    PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200,
)
from .post_crm_funnels_funnel_id_custom_fields_custom_field_id_options_response_200 import (
    PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsResponse200,
)
from .post_crm_funnels_funnel_id_custom_fields_id_move_body import PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody
from .post_crm_funnels_funnel_id_custom_fields_id_move_response_200 import (
    PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200,
)
from .post_crm_funnels_funnel_id_custom_fields_response_200 import PostCrmFunnelsFunnelIdCustomFieldsResponse200
from .post_crm_organizations_organization_id_addresses_body import PostCrmOrganizationsOrganizationIdAddressesBody
from .post_crm_organizations_organization_id_contacts_body import PostCrmOrganizationsOrganizationIdContactsBody
from .post_crm_organizations_organization_id_emails_body import PostCrmOrganizationsOrganizationIdEmailsBody
from .post_crm_organizations_organization_id_phones_body import PostCrmOrganizationsOrganizationIdPhonesBody
from .post_crm_organizations_organization_id_tags_body import PostCrmOrganizationsOrganizationIdTagsBody
from .post_tm_board_columns_body import PostTmBoardColumnsBody
from .post_tm_board_columns_id_move_body import PostTmBoardColumnsIdMoveBody
from .post_tm_board_columns_id_move_response_200 import PostTmBoardColumnsIdMoveResponse200
from .post_tm_board_columns_response_200 import PostTmBoardColumnsResponse200
from .post_tm_boards_body import PostTmBoardsBody
from .post_tm_boards_id_move_body import PostTmBoardsIdMoveBody
from .post_tm_boards_id_move_response_200 import PostTmBoardsIdMoveResponse200
from .post_tm_boards_response_200 import PostTmBoardsResponse200
from .post_tm_projects_body import PostTmProjectsBody
from .post_tm_projects_id_archive_response_200 import PostTmProjectsIdArchiveResponse200
from .post_tm_projects_id_un_archive_response_200 import PostTmProjectsIdUnArchiveResponse200
from .post_tm_projects_project_id_custom_fields_custom_field_id_options_id_move_body import (
    PostTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdMoveBody,
)
from .post_tm_projects_project_id_custom_fields_custom_field_id_options_id_move_response_200 import (
    PostTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200,
)
from .post_tm_projects_project_id_custom_fields_custom_field_id_options_response_200 import (
    PostTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsResponse200,
)
from .post_tm_projects_project_id_custom_fields_id_move_body import PostTmProjectsProjectIdCustomFieldsIdMoveBody
from .post_tm_projects_project_id_custom_fields_id_move_response_200 import (
    PostTmProjectsProjectIdCustomFieldsIdMoveResponse200,
)
from .post_tm_projects_project_id_custom_fields_response_200 import PostTmProjectsProjectIdCustomFieldsResponse200
from .post_tm_projects_response_200 import PostTmProjectsResponse200
from .post_tm_tasks_body import PostTmTasksBody
from .post_tm_tasks_body_custom_fields import PostTmTasksBodyCustomFields
from .post_tm_tasks_body_priority import PostTmTasksBodyPriority
from .post_tm_tasks_body_type import PostTmTasksBodyType
from .post_tm_tasks_id_board_body import PostTmTasksIdBoardBody
from .post_tm_tasks_id_board_column_body import PostTmTasksIdBoardColumnBody
from .post_tm_tasks_id_board_column_response_200 import PostTmTasksIdBoardColumnResponse200
from .post_tm_tasks_id_board_response_200 import PostTmTasksIdBoardResponse200
from .post_tm_tasks_id_complete_response_200 import PostTmTasksIdCompleteResponse200
from .post_tm_tasks_id_un_complete_response_200 import PostTmTasksIdUnCompleteResponse200
from .post_tm_tasks_response_200 import PostTmTasksResponse200
from .post_tm_tasks_task_id_attachments_body import PostTmTasksTaskIdAttachmentsBody
from .post_tm_tasks_task_id_attachments_response_200 import PostTmTasksTaskIdAttachmentsResponse200
from .post_tm_tasks_task_id_time_entries_response_200 import PostTmTasksTaskIdTimeEntriesResponse200
from .post_tm_tasks_task_id_watchers_response_200 import PostTmTasksTaskIdWatchersResponse200
from .post_ws_tags_body import PostWsTagsBody
from .post_ws_tags_response_200 import PostWsTagsResponse200
from .project import Project
from .put_crm_contacts_contact_id_emails_email_id_body import PutCrmContactsContactIdEmailsEmailIdBody
from .put_crm_contacts_contacts_id_phones_phone_id_body import PutCrmContactsContactsIdPhonesPhoneIdBody
from .put_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_response_200 import (
    PutCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdResponse200,
)
from .put_crm_funnels_funnel_id_custom_fields_id_response_200 import PutCrmFunnelsFunnelIdCustomFieldsIdResponse200
from .put_crm_organizations_organization_id_addresses_address_id_body import (
    PutCrmOrganizationsOrganizationIdAddressesAddressIdBody,
)
from .put_crm_organizations_organization_id_emails_email_id_body import (
    PutCrmOrganizationsOrganizationIdEmailsEmailIdBody,
)
from .put_crm_organizations_organization_id_phones_phone_id_body import (
    PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody,
)
from .put_tm_board_columns_id_body import PutTmBoardColumnsIdBody
from .put_tm_board_columns_id_response_200 import PutTmBoardColumnsIdResponse200
from .put_tm_boards_id_body import PutTmBoardsIdBody
from .put_tm_boards_id_response_200 import PutTmBoardsIdResponse200
from .put_tm_projects_id_body import PutTmProjectsIdBody
from .put_tm_projects_id_response_200 import PutTmProjectsIdResponse200
from .put_tm_projects_project_id_custom_fields_custom_field_id_options_id_response_200 import (
    PutTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200,
)
from .put_tm_projects_project_id_custom_fields_id_response_200 import PutTmProjectsProjectIdCustomFieldsIdResponse200
from .put_tm_tasks_id_response_200 import PutTmTasksIdResponse200
from .put_tm_tasks_task_id_time_entries_time_entry_id_response_200 import (
    PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200,
)
from .put_ws_tags_id_body import PutWsTagsIdBody
from .put_ws_tags_id_response_200 import PutWsTagsIdResponse200
from .successful_response import SuccessfulResponse
from .tag import Tag
from .task import Task
from .task_type import TaskType
from .task_update_request import TaskUpdateRequest
from .task_update_request_custom_fields import TaskUpdateRequestCustomFields
from .task_update_request_priority import TaskUpdateRequestPriority
from .task_update_request_type import TaskUpdateRequestType
from .task_workloads_item import TaskWorkloadsItem
from .task_workloads_item_type import TaskWorkloadsItemType
from .time_entry import TimeEntry
from .time_entry_request import TimeEntryRequest
from .time_entry_type import TimeEntryType
from .user import User
from .watchers import Watchers
from .workspace import Workspace

__all__ = (
    "AddressResponse",
    "ApiResponse",
    "Attachment",
    "AttachmentServiceEnum",
    "Board",
    "BoardColumn",
    "Contact",
    "ContactEmail",
    "ContactPhone",
    "CrmContact",
    "CrmContact1",
    "CrmContacts",
    "CrmCurrencies",
    "CrmDeal",
    "CrmDealAttachTaskResponse200",
    "CrmDeals",
    "CrmFunnel",
    "CrmFunnels",
    "CrmFunnelStatus",
    "CrmFunnelStatuses",
    "CrmMoveAttachedDealTaskBody",
    "CrmMoveDealBody",
    "CrmOrganization",
    "CrmOrganization1",
    "CrmOrganizations",
    "CrmUpdateDealFunnelBody",
    "CrmUpdateDealStatusBody",
    "Currency",
    "CurrentUser",
    "CustomField",
    "CustomFieldConfigType0",
    "CustomFieldConfigType0Type",
    "CustomFieldCreateBody",
    "CustomFieldCreateBodyConfigType0",
    "CustomFieldCreateBodyConfigType0Type",
    "CustomFieldCreateBodyType",
    "CustomFieldOption",
    "CustomFieldOption1",
    "CustomFieldOption1Color",
    "CustomFieldOptionColor",
    "CustomFieldType",
    "CustomFieldUpdateBody",
    "CustomFieldUpdateBodyConfigType0",
    "CustomFieldUpdateBodyConfigType0Type",
    "CustomFieldValue",
    "CustomFieldValueConfigType0",
    "CustomFieldValueConfigType0Type",
    "CustomFieldValues",
    "CustomFieldValueType",
    "Deal",
    "DealCreateRequest",
    "DealCreateRequestWinStatus",
    "DealUpdateRequest",
    "DealUpdateRequestWinStatus",
    "DealWinStatus",
    "DeleteCrmContactsContactIdTagsBody",
    "DeleteCrmDealsDealIdAssigneesBody",
    "DeleteCrmDealsDealIdContactsBody",
    "DeleteCrmDealsDealIdOrganizationsBody",
    "DeleteCrmDealsDealIdTagsBody",
    "DeleteCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdResponse200",
    "DeleteCrmFunnelsFunnelIdCustomFieldsIdResponse200",
    "DeleteCrmOrganizationsOrganizationIdContactsBody",
    "DeleteCrmOrganizationsOrganizationIdTagsBody",
    "DeleteTmBoardColumnsIdResponse200",
    "DeleteTmBoardsIdResponse200",
    "DeleteTmProjectsIdResponse200",
    "DeleteTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200",
    "DeleteTmProjectsProjectIdCustomFieldsIdResponse200",
    "DeleteTmTasksIdResponse200",
    "DeleteTmTasksTaskIdTimeEntriesTimeEntryIdResponse200",
    "DeleteTmTasksTaskIdWatchersResponse200",
    "DeleteWsTags2Response200",
    "EmailResponse",
    "EmailResponse1",
    "Funnel",
    "FunnelManageRequest",
    "FunnelStatus",
    "FunnelStatusManageRequest",
    "GetAttachmentsAttachmentIdResponse200",
    "GetTmBoardColumnsResponse200",
    "GetTmBoardsResponse200",
    "GetTmProjectsIdResponse200",
    "GetTmProjectsResponse200",
    "GetTmTasksIdResponse200",
    "GetTmTasksResponse200",
    "GetUserMeResponse200",
    "GetWsMembersResponse200",
    "GetWsResponse200",
    "GetWsTagsIdResponse200",
    "GetWsTagsResponse200",
    "Organization",
    "OrganizationAddress",
    "OrganizationEmail",
    "OrganizationPhone",
    "PhoneResponse",
    "PhoneResponse1",
    "PostCrmContactsContactIdEmailsBody",
    "PostCrmContactsContactIdTagsBody",
    "PostCrmContactsContactsIdPhonesBody",
    "PostCrmDealsDealIdAssigneesBody",
    "PostCrmDealsDealIdAttachmentsBody",
    "PostCrmDealsDealIdAttachmentsResponse200",
    "PostCrmDealsDealIdContactsBody",
    "PostCrmDealsDealIdOrganizationsBody",
    "PostCrmDealsDealIdTagsBody",
    "PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveBody",
    "PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200",
    "PostCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsResponse200",
    "PostCrmFunnelsFunnelIdCustomFieldsIdMoveBody",
    "PostCrmFunnelsFunnelIdCustomFieldsIdMoveResponse200",
    "PostCrmFunnelsFunnelIdCustomFieldsResponse200",
    "PostCrmOrganizationsOrganizationIdAddressesBody",
    "PostCrmOrganizationsOrganizationIdContactsBody",
    "PostCrmOrganizationsOrganizationIdEmailsBody",
    "PostCrmOrganizationsOrganizationIdPhonesBody",
    "PostCrmOrganizationsOrganizationIdTagsBody",
    "PostTmBoardColumnsBody",
    "PostTmBoardColumnsIdMoveBody",
    "PostTmBoardColumnsIdMoveResponse200",
    "PostTmBoardColumnsResponse200",
    "PostTmBoardsBody",
    "PostTmBoardsIdMoveBody",
    "PostTmBoardsIdMoveResponse200",
    "PostTmBoardsResponse200",
    "PostTmProjectsBody",
    "PostTmProjectsIdArchiveResponse200",
    "PostTmProjectsIdUnArchiveResponse200",
    "PostTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdMoveBody",
    "PostTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdMoveResponse200",
    "PostTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsResponse200",
    "PostTmProjectsProjectIdCustomFieldsIdMoveBody",
    "PostTmProjectsProjectIdCustomFieldsIdMoveResponse200",
    "PostTmProjectsProjectIdCustomFieldsResponse200",
    "PostTmProjectsResponse200",
    "PostTmTasksBody",
    "PostTmTasksBodyCustomFields",
    "PostTmTasksBodyPriority",
    "PostTmTasksBodyType",
    "PostTmTasksIdBoardBody",
    "PostTmTasksIdBoardColumnBody",
    "PostTmTasksIdBoardColumnResponse200",
    "PostTmTasksIdBoardResponse200",
    "PostTmTasksIdCompleteResponse200",
    "PostTmTasksIdUnCompleteResponse200",
    "PostTmTasksResponse200",
    "PostTmTasksTaskIdAttachmentsBody",
    "PostTmTasksTaskIdAttachmentsResponse200",
    "PostTmTasksTaskIdTimeEntriesResponse200",
    "PostTmTasksTaskIdWatchersResponse200",
    "PostWsTagsBody",
    "PostWsTagsResponse200",
    "Project",
    "PutCrmContactsContactIdEmailsEmailIdBody",
    "PutCrmContactsContactsIdPhonesPhoneIdBody",
    "PutCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdResponse200",
    "PutCrmFunnelsFunnelIdCustomFieldsIdResponse200",
    "PutCrmOrganizationsOrganizationIdAddressesAddressIdBody",
    "PutCrmOrganizationsOrganizationIdEmailsEmailIdBody",
    "PutCrmOrganizationsOrganizationIdPhonesPhoneIdBody",
    "PutTmBoardColumnsIdBody",
    "PutTmBoardColumnsIdResponse200",
    "PutTmBoardsIdBody",
    "PutTmBoardsIdResponse200",
    "PutTmProjectsIdBody",
    "PutTmProjectsIdResponse200",
    "PutTmProjectsProjectIdCustomFieldsCustomFieldIdOptionsIdResponse200",
    "PutTmProjectsProjectIdCustomFieldsIdResponse200",
    "PutTmTasksIdResponse200",
    "PutTmTasksTaskIdTimeEntriesTimeEntryIdResponse200",
    "PutWsTagsIdBody",
    "PutWsTagsIdResponse200",
    "SuccessfulResponse",
    "Tag",
    "Task",
    "TaskType",
    "TaskUpdateRequest",
    "TaskUpdateRequestCustomFields",
    "TaskUpdateRequestPriority",
    "TaskUpdateRequestType",
    "TaskWorkloadsItem",
    "TaskWorkloadsItemType",
    "TimeEntry",
    "TimeEntryRequest",
    "TimeEntryType",
    "User",
    "Watchers",
    "Workspace",
)
