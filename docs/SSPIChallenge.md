# SSPIChallenge

Thrown during SSPI pass-through authentication if further negotiation is required.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_token** | **str** | The opaque server response token, base-64 encoded.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.sspi_challenge import SSPIChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of SSPIChallenge from a JSON string
sspi_challenge_instance = SSPIChallenge.from_json(json)
# print the JSON string representation of the object
print SSPIChallenge.to_json()

# convert the object into a dict
sspi_challenge_dict = sspi_challenge_instance.to_dict()
# create an instance of SSPIChallenge from a dict
sspi_challenge_form_dict = sspi_challenge.from_dict(sspi_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


