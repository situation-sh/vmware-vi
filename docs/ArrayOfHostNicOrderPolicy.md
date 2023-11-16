# ArrayOfHostNicOrderPolicy

A boxed array of *HostNicOrderPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNicOrderPolicy]**](HostNicOrderPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nic_order_policy import ArrayOfHostNicOrderPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNicOrderPolicy from a JSON string
array_of_host_nic_order_policy_instance = ArrayOfHostNicOrderPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNicOrderPolicy.to_json()

# convert the object into a dict
array_of_host_nic_order_policy_dict = array_of_host_nic_order_policy_instance.to_dict()
# create an instance of ArrayOfHostNicOrderPolicy from a dict
array_of_host_nic_order_policy_form_dict = array_of_host_nic_order_policy.from_dict(array_of_host_nic_order_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


