# ArrayOfSingleIp

A boxed array of *SingleIp*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SingleIp]**](SingleIp.md) |  | 

## Example

```python
from vmware_vi.models.array_of_single_ip import ArrayOfSingleIp

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSingleIp from a JSON string
array_of_single_ip_instance = ArrayOfSingleIp.from_json(json)
# print the JSON string representation of the object
print ArrayOfSingleIp.to_json()

# convert the object into a dict
array_of_single_ip_dict = array_of_single_ip_instance.to_dict()
# create an instance of ArrayOfSingleIp from a dict
array_of_single_ip_form_dict = array_of_single_ip.from_dict(array_of_single_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


