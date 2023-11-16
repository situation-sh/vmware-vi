# DvsOutOfSyncHostArgument

The host on which the DVS configuration is different from that of Virtual Center server.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**out_of_sync_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**config_paramters** | **List[str]** | The DVS configuration parameters that are different between Virtual Center server and the host.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dvs_out_of_sync_host_argument import DvsOutOfSyncHostArgument

# TODO update the JSON string below
json = "{}"
# create an instance of DvsOutOfSyncHostArgument from a JSON string
dvs_out_of_sync_host_argument_instance = DvsOutOfSyncHostArgument.from_json(json)
# print the JSON string representation of the object
print DvsOutOfSyncHostArgument.to_json()

# convert the object into a dict
dvs_out_of_sync_host_argument_dict = dvs_out_of_sync_host_argument_instance.to_dict()
# create an instance of DvsOutOfSyncHostArgument from a dict
dvs_out_of_sync_host_argument_form_dict = dvs_out_of_sync_host_argument.from_dict(dvs_out_of_sync_host_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


