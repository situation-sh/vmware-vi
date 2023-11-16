# ArrayOfSSPIChallenge

A boxed array of *SSPIChallenge*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SSPIChallenge]**](SSPIChallenge.md) |  | 

## Example

```python
from vmware_vi.models.array_of_sspi_challenge import ArrayOfSSPIChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSSPIChallenge from a JSON string
array_of_sspi_challenge_instance = ArrayOfSSPIChallenge.from_json(json)
# print the JSON string representation of the object
print ArrayOfSSPIChallenge.to_json()

# convert the object into a dict
array_of_sspi_challenge_dict = array_of_sspi_challenge_instance.to_dict()
# create an instance of ArrayOfSSPIChallenge from a dict
array_of_sspi_challenge_form_dict = array_of_sspi_challenge.from_dict(array_of_sspi_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


