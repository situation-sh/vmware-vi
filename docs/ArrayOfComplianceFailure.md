# ArrayOfComplianceFailure

A boxed array of *ComplianceFailure*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ComplianceFailure]**](ComplianceFailure.md) |  | 

## Example

```python
from vmware_vi.models.array_of_compliance_failure import ArrayOfComplianceFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfComplianceFailure from a JSON string
array_of_compliance_failure_instance = ArrayOfComplianceFailure.from_json(json)
# print the JSON string representation of the object
print ArrayOfComplianceFailure.to_json()

# convert the object into a dict
array_of_compliance_failure_dict = array_of_compliance_failure_instance.to_dict()
# create an instance of ArrayOfComplianceFailure from a dict
array_of_compliance_failure_form_dict = array_of_compliance_failure.from_dict(array_of_compliance_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


