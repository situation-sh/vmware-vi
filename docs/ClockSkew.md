# ClockSkew

Fault indicating that the clock skew in the system exceeds the limit.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.clock_skew import ClockSkew

# TODO update the JSON string below
json = "{}"
# create an instance of ClockSkew from a JSON string
clock_skew_instance = ClockSkew.from_json(json)
# print the JSON string representation of the object
print ClockSkew.to_json()

# convert the object into a dict
clock_skew_dict = clock_skew_instance.to_dict()
# create an instance of ClockSkew from a dict
clock_skew_form_dict = clock_skew.from_dict(clock_skew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


