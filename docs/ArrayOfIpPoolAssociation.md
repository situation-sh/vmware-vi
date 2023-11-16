# ArrayOfIpPoolAssociation

A boxed array of *IpPoolAssociation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IpPoolAssociation]**](IpPoolAssociation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ip_pool_association import ArrayOfIpPoolAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIpPoolAssociation from a JSON string
array_of_ip_pool_association_instance = ArrayOfIpPoolAssociation.from_json(json)
# print the JSON string representation of the object
print ArrayOfIpPoolAssociation.to_json()

# convert the object into a dict
array_of_ip_pool_association_dict = array_of_ip_pool_association_instance.to_dict()
# create an instance of ArrayOfIpPoolAssociation from a dict
array_of_ip_pool_association_form_dict = array_of_ip_pool_association.from_dict(array_of_ip_pool_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


