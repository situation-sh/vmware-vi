# CreateDVPortgroupRequestType

The parameters of *DistributedVirtualSwitch.CreateDVPortgroup_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**DVPortgroupConfigSpec**](DVPortgroupConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_dv_portgroup_request_type import CreateDVPortgroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDVPortgroupRequestType from a JSON string
create_dv_portgroup_request_type_instance = CreateDVPortgroupRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDVPortgroupRequestType.to_json()

# convert the object into a dict
create_dv_portgroup_request_type_dict = create_dv_portgroup_request_type_instance.to_dict()
# create an instance of CreateDVPortgroupRequestType from a dict
create_dv_portgroup_request_type_form_dict = create_dv_portgroup_request_type.from_dict(create_dv_portgroup_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


