# HostFlagInfo

The FlagInfo data object type encapsulates the flag settings for a host.  These properties are optional since the same structure is used to change the values during an edit or create operation.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_snapshots_enabled** | **bool** | Flag to specify whether background snapshots are enabled.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.host_flag_info import HostFlagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostFlagInfo from a JSON string
host_flag_info_instance = HostFlagInfo.from_json(json)
# print the JSON string representation of the object
print HostFlagInfo.to_json()

# convert the object into a dict
host_flag_info_dict = host_flag_info_instance.to_dict()
# create an instance of HostFlagInfo from a dict
host_flag_info_form_dict = host_flag_info.from_dict(host_flag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


