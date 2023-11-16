# DvsHostStatusUpdated

A host has it's status or statusDetail updated.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_member** | [**HostEventArgument**](HostEventArgument.md) |  | 
**old_status** | **str** | Host&#39;s old status.  ***Since:*** vSphere API 4.1  | [optional] 
**new_status** | **str** | Host&#39;s new status.  ***Since:*** vSphere API 4.1  | [optional] 
**old_status_detail** | **str** | Comments regarding host&#39;s old status.  ***Since:*** vSphere API 4.1  | [optional] 
**new_status_detail** | **str** | Comments regarding host&#39;s new status.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.dvs_host_status_updated import DvsHostStatusUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHostStatusUpdated from a JSON string
dvs_host_status_updated_instance = DvsHostStatusUpdated.from_json(json)
# print the JSON string representation of the object
print DvsHostStatusUpdated.to_json()

# convert the object into a dict
dvs_host_status_updated_dict = dvs_host_status_updated_instance.to_dict()
# create an instance of DvsHostStatusUpdated from a dict
dvs_host_status_updated_form_dict = dvs_host_status_updated.from_dict(dvs_host_status_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


