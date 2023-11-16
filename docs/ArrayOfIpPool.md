# ArrayOfIpPool

A boxed array of *IpPool*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IpPool]**](IpPool.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ip_pool import ArrayOfIpPool

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIpPool from a JSON string
array_of_ip_pool_instance = ArrayOfIpPool.from_json(json)
# print the JSON string representation of the object
print ArrayOfIpPool.to_json()

# convert the object into a dict
array_of_ip_pool_dict = array_of_ip_pool_instance.to_dict()
# create an instance of ArrayOfIpPool from a dict
array_of_ip_pool_form_dict = array_of_ip_pool.from_dict(array_of_ip_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


