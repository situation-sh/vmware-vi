# HostListSummary

This data object type encapsulates a typical set of host information that is useful for list views and summary pages.  VirtualCenter can retrieve this information very efficiently, even for a large set of hosts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**hardware** | [**HostHardwareSummary**](HostHardwareSummary.md) |  | [optional] 
**runtime** | [**HostRuntimeInfo**](HostRuntimeInfo.md) |  | [optional] 
**config** | [**HostConfigSummary**](HostConfigSummary.md) |  | 
**quick_stats** | [**HostListSummaryQuickStats**](HostListSummaryQuickStats.md) |  | 
**overall_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**reboot_required** | **bool** | Indicates whether or not the host requires a reboot due to a configuration change.  | 
**custom_value** | [**List[CustomFieldValue]**](CustomFieldValue.md) | The customized field values.  | [optional] 
**management_server_ip** | **str** | IP address of the VirtualCenter server managing this host, if any.  ***Since:*** VI API 2.5  | [optional] 
**max_evc_mode_key** | **str** | The most capable Enhanced VMotion Compatibility mode supported by the host hardware and software; unset if this host cannot participate in any EVC mode.  See also *Capability.supportedEVCMode*.  ***Since:*** vSphere API 4.0  | [optional] 
**current_evc_mode_key** | **str** | The Enhanced VMotion Compatibility mode that is currently in effect for this host.  If the host is in a cluster where EVC is active, this will match the cluster&#39;s EVC mode; otherwise this will be unset.  See also *Capability.supportedEVCMode*.  ***Since:*** vSphere API 4.0  | [optional] 
**current_evc_graphics_mode_key** | **str** | The Enhanced VMotion Compatibility Graphics mode that is currently in effect for this host.  If the host is in a cluster where EVC is active, this will match the cluster&#39;s EVC Graphics mode; otherwise this will be unset.  See also *Capability.supportedEVCGraphicsMode*.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**gateway** | [**HostListSummaryGatewaySummary**](HostListSummaryGatewaySummary.md) |  | [optional] 
**tpm_attestation** | [**HostTpmAttestationInfo**](HostTpmAttestationInfo.md) |  | [optional] 
**trust_authority_attestation_infos** | [**List[HostTrustAuthorityAttestationInfo]**](HostTrustAuthorityAttestationInfo.md) | The attestation information for the host as retrieved from any Trust Authority attestation services configured in the host&#39;s parent compute resource.  This field will be set only if there is any Trust Authority attestation service configured for the host&#39;s parent compute resource, and unset otherwise.  ***Since:*** vSphere API 7.0.1.0  | [optional] 

## Example

```python
from vmware_vi.models.host_list_summary import HostListSummary

# TODO update the JSON string below
json = "{}"
# create an instance of HostListSummary from a JSON string
host_list_summary_instance = HostListSummary.from_json(json)
# print the JSON string representation of the object
print HostListSummary.to_json()

# convert the object into a dict
host_list_summary_dict = host_list_summary_instance.to_dict()
# create an instance of HostListSummary from a dict
host_list_summary_form_dict = host_list_summary.from_dict(host_list_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


