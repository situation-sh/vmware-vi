# ArrayOfFaultDomainId

A boxed array of *FaultDomainId*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FaultDomainId]**](FaultDomainId.md) |  | 

## Example

```python
from vmware_vi.models.array_of_fault_domain_id import ArrayOfFaultDomainId

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFaultDomainId from a JSON string
array_of_fault_domain_id_instance = ArrayOfFaultDomainId.from_json(json)
# print the JSON string representation of the object
print ArrayOfFaultDomainId.to_json()

# convert the object into a dict
array_of_fault_domain_id_dict = array_of_fault_domain_id_instance.to_dict()
# create an instance of ArrayOfFaultDomainId from a dict
array_of_fault_domain_id_form_dict = array_of_fault_domain_id.from_dict(array_of_fault_domain_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


