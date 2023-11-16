# GuestComponentsOutOfDate

A GuestComponentsOutOfDate exception is thrown when an operation fails because the guest operations agent is out of date and lacks the functionality to execute the operation.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_components_out_of_date import GuestComponentsOutOfDate

# TODO update the JSON string below
json = "{}"
# create an instance of GuestComponentsOutOfDate from a JSON string
guest_components_out_of_date_instance = GuestComponentsOutOfDate.from_json(json)
# print the JSON string representation of the object
print GuestComponentsOutOfDate.to_json()

# convert the object into a dict
guest_components_out_of_date_dict = guest_components_out_of_date_instance.to_dict()
# create an instance of GuestComponentsOutOfDate from a dict
guest_components_out_of_date_form_dict = guest_components_out_of_date.from_dict(guest_components_out_of_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


