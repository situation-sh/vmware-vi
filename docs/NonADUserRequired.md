# NonADUserRequired

Fault indicating that an operation must be executed by a non Active Directory user.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.non_ad_user_required import NonADUserRequired

# TODO update the JSON string below
json = "{}"
# create an instance of NonADUserRequired from a JSON string
non_ad_user_required_instance = NonADUserRequired.from_json(json)
# print the JSON string representation of the object
print NonADUserRequired.to_json()

# convert the object into a dict
non_ad_user_required_dict = non_ad_user_required_instance.to_dict()
# create an instance of NonADUserRequired from a dict
non_ad_user_required_form_dict = non_ad_user_required.from_dict(non_ad_user_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


