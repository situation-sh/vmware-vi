# ArrayOfComplianceLocator

A boxed array of *ComplianceLocator*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ComplianceLocator]**](ComplianceLocator.md) |  | 

## Example

```python
from vmware_vi.models.array_of_compliance_locator import ArrayOfComplianceLocator

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfComplianceLocator from a JSON string
array_of_compliance_locator_instance = ArrayOfComplianceLocator.from_json(json)
# print the JSON string representation of the object
print ArrayOfComplianceLocator.to_json()

# convert the object into a dict
array_of_compliance_locator_dict = array_of_compliance_locator_instance.to_dict()
# create an instance of ArrayOfComplianceLocator from a dict
array_of_compliance_locator_form_dict = array_of_compliance_locator.from_dict(array_of_compliance_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


