# ReconfigureDVPortgroupRequestType

The parameters of *DistributedVirtualPortgroup.ReconfigureDVPortgroup_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**DVPortgroupConfigSpec**](DVPortgroupConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.reconfigure_dv_portgroup_request_type import ReconfigureDVPortgroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureDVPortgroupRequestType from a JSON string
reconfigure_dv_portgroup_request_type_instance = ReconfigureDVPortgroupRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureDVPortgroupRequestType.to_json()

# convert the object into a dict
reconfigure_dv_portgroup_request_type_dict = reconfigure_dv_portgroup_request_type_instance.to_dict()
# create an instance of ReconfigureDVPortgroupRequestType from a dict
reconfigure_dv_portgroup_request_type_form_dict = reconfigure_dv_portgroup_request_type.from_dict(reconfigure_dv_portgroup_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


