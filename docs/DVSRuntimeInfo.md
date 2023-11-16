# DVSRuntimeInfo

The *DVSRuntimeInfo* data object defines runtime information for a vSphere Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_member_runtime** | [**List[HostMemberRuntimeInfo]**](HostMemberRuntimeInfo.md) | Runtime information of the hosts that joined the switch.  ***Since:*** vSphere API 5.1  | [optional] 
**resource_runtime_info** | [**DvsResourceRuntimeInfo**](DvsResourceRuntimeInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_runtime_info import DVSRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DVSRuntimeInfo from a JSON string
dvs_runtime_info_instance = DVSRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print DVSRuntimeInfo.to_json()

# convert the object into a dict
dvs_runtime_info_dict = dvs_runtime_info_instance.to_dict()
# create an instance of DVSRuntimeInfo from a dict
dvs_runtime_info_form_dict = dvs_runtime_info.from_dict(dvs_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


