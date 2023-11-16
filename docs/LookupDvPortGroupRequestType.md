# LookupDvPortGroupRequestType

The parameters of *DistributedVirtualSwitch.LookupDvPortGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgroup_key** | **str** | The key that identifies a portgroup of this VDS.  | 

## Example

```python
from vmware_vi.models.lookup_dv_port_group_request_type import LookupDvPortGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of LookupDvPortGroupRequestType from a JSON string
lookup_dv_port_group_request_type_instance = LookupDvPortGroupRequestType.from_json(json)
# print the JSON string representation of the object
print LookupDvPortGroupRequestType.to_json()

# convert the object into a dict
lookup_dv_port_group_request_type_dict = lookup_dv_port_group_request_type_instance.to_dict()
# create an instance of LookupDvPortGroupRequestType from a dict
lookup_dv_port_group_request_type_form_dict = lookup_dv_port_group_request_type.from_dict(lookup_dv_port_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


