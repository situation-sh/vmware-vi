# HostAccessControlEntry

Data structure describing the access mode for a user or group.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal** | **str** | User or group having the described access mode.  The format is \&quot;login\&quot; for local users or \&quot;DOMAIN\\\\login\&quot; for users in a Windows domain.  ***Since:*** vSphere API 6.0  | 
**group** | **bool** | True if &#39;principal&#39; describes a group account, false otherwise.  ***Since:*** vSphere API 6.0  | 
**access_mode** | [**HostAccessModeEnum**](HostAccessModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_access_control_entry import HostAccessControlEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HostAccessControlEntry from a JSON string
host_access_control_entry_instance = HostAccessControlEntry.from_json(json)
# print the JSON string representation of the object
print HostAccessControlEntry.to_json()

# convert the object into a dict
host_access_control_entry_dict = host_access_control_entry_instance.to_dict()
# create an instance of HostAccessControlEntry from a dict
host_access_control_entry_form_dict = host_access_control_entry.from_dict(host_access_control_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


