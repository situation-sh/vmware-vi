# CustomizationSysprepText

An alternate way to specify the `sysprep.xml` answer file.  This string is written to the `sysprep.xml` answer file on the target virtual disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Text for the &#x60;sysprep.xml&#x60; answer file.  For additional details, see &lt;a href&#x3D;\&quot;https://kb.vmware.com/selfservice/microsites/search.do?language&#x3D;en_US&amp;cmd&#x3D;displayKC&amp;externalId&#x3D;2151684\&quot;target&#x3D;\&quot;_blank\&quot;&gt;Using custom sysprep.xml for vCenter Guest Customization&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://kb.vmware.com/selfservice/microsites/search.do?language&#x3D;en_US&amp;cmd&#x3D;displayKC&amp;externalId&#x3D;1029174\&quot;target&#x3D;\&quot;_blank\&quot;&gt;Specifying network settings in custom sysprep.xml&lt;/a&gt;.  | 

## Example

```python
from vmware_vi.models.customization_sysprep_text import CustomizationSysprepText

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSysprepText from a JSON string
customization_sysprep_text_instance = CustomizationSysprepText.from_json(json)
# print the JSON string representation of the object
print CustomizationSysprepText.to_json()

# convert the object into a dict
customization_sysprep_text_dict = customization_sysprep_text_instance.to_dict()
# create an instance of CustomizationSysprepText from a dict
customization_sysprep_text_form_dict = customization_sysprep_text.from_dict(customization_sysprep_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


