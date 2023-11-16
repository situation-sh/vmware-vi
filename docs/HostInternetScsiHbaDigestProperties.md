# HostInternetScsiHbaDigestProperties

The digest settings for this host bus adapter.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_digest_type** | **str** | The header digest preference if header digest is enabled  ***Since:*** vSphere API 4.0  | [optional] 
**header_digest_inherited** | **bool** | Header digest setting is inherited  ***Since:*** vSphere API 4.0  | [optional] 
**data_digest_type** | **str** | The data digest preference if data digest is enabled  ***Since:*** vSphere API 4.0  | [optional] 
**data_digest_inherited** | **bool** | Data digest setting is inherited  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_digest_properties import HostInternetScsiHbaDigestProperties

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaDigestProperties from a JSON string
host_internet_scsi_hba_digest_properties_instance = HostInternetScsiHbaDigestProperties.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaDigestProperties.to_json()

# convert the object into a dict
host_internet_scsi_hba_digest_properties_dict = host_internet_scsi_hba_digest_properties_instance.to_dict()
# create an instance of HostInternetScsiHbaDigestProperties from a dict
host_internet_scsi_hba_digest_properties_form_dict = host_internet_scsi_hba_digest_properties.from_dict(host_internet_scsi_hba_digest_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


