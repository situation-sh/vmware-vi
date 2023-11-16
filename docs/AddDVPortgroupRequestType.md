# AddDVPortgroupRequestType

The parameters of *DistributedVirtualSwitch.AddDVPortgroup_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**List[DVPortgroupConfigSpec]**](DVPortgroupConfigSpec.md) | The specification for the portgroup.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.add_dv_portgroup_request_type import AddDVPortgroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddDVPortgroupRequestType from a JSON string
add_dv_portgroup_request_type_instance = AddDVPortgroupRequestType.from_json(json)
# print the JSON string representation of the object
print AddDVPortgroupRequestType.to_json()

# convert the object into a dict
add_dv_portgroup_request_type_dict = add_dv_portgroup_request_type_instance.to_dict()
# create an instance of AddDVPortgroupRequestType from a dict
add_dv_portgroup_request_type_form_dict = add_dv_portgroup_request_type.from_dict(add_dv_portgroup_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


