goog.provide('Blockly.MyCustomField');
goog.require('Blockly.FieldNumber');

Blockly.MyCustomField = function(opt_value, opt_min, opt_max, opt_precision, opt_validator, opt_config) {
    //opt_value = this.doClassValidation_(opt_value);
    if (opt_value === null) {
        opt_value = Blockly.MyCustomField.DEFAULT_VALUE;
    }  // Else the original value is fine.
    Blockly.MyCustomField.superClass_.constructor.call((this, opt_min, opt_max, opt_precision, opt_validator, opt_config);
};

goog.inherits(Blockly.MyCustomField, Blockly.FieldNumber);