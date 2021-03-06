/*! Copyright 2009 Tim Savage <tim.savage@jooceylabs.com>
 * Licensed under the BSD license (http://www.opensource.org/licenses/bsd-license.php)
 *
 * Version: 0.2
 * Requires jQuery 1.2.6+
 * Docs: http://code.google.com/p/django-ajax-forms/
 *
 * Validation methods, additional functions can be added to preform
 * custom validation eg:
 * $.fn.validation.rules['foo'] = function(field, arg, value, msgs) {
 *     if (validation fail) {
 *         throw new $.validation.ValidationError(msgs['msg_code']);
 *     }
 * };
 */

(function($) {

    var ValidationError = $.validation.ValidationError;

    // Regular expressions see http://regexpal.com/
    var DECIMAL_LENGTHS = /^[-\s0]*(\d*).?(\d*)\s*$/;
    var IS_FLOAT = /^-?\d*(\.?\d*)$/;
    var IS_INTEGER = /^-?\d+$/;
    var IS_DATE = '^(\\d{4}-((0?\\d)|(1[0-2]))-(([0-2]\\d)|(3[01])))$|' +
        '^((([0-2]?[0-9])|(3[01]))/((0?\\d)|(1[0-2]))/(\\d{2}|\\d{4}))$';
    var IS_TIME = '^(([0-1]\\d)|(2[0-3])|\\d)(:[0-5]?\\d)(:[0-5]?\\d)?$';
    var IS_DATETIME = '^((\\d{4}-((0?\\d)|(1[0-2]))-(([0-2]?\\d)|(3[01])))|' +
        '(((0?\\d)|(1[0-2]))/(([0-2]?\\d)|(3[01]))/(\\d{2}|\\d{4})?))' +
        '( (([0-1]\\d)|(2[0-3])|\\d)(:[0-5]?\\d)(:[0-5]?\\d)?)?$';


    $.extend($.validation.rules, {

        max_length: function(field, arg, value, msgs) {
            if (value.length > arg) {
                throw new ValidationError(msgs['max_length'], {
                    '%(limit_value)s': arg,
                    '%(length)d': value.length
                });
            }
        },

        min_length: function(field, arg, value, msgs) {
            if (value.length < arg) {
                throw new ValidationError(msgs['min_length'], {
                    '%(limit_value)s': arg,
                    '%(length)d': value.length
                });
            }
        },

        decimal_length: function(field, arg, value, msgs) {
            var match = DECIMAL_LENGTHS.exec(value);
            if (match) {
                var max_digits = arg[0];
                if (max_digits !== null && (match[1].length + match[2].length) > max_digits) {
                    throw new ValidationError(msgs['max_digits'], {
                        '%s': max_digits
                    });
                }

                var max_decimal_places = arg[1];
                if (max_decimal_places !== null && match[2].length > max_decimal_places) {
                    throw new ValidationError(msgs['max_decimal_places'], {
                        '%s': max_decimal_places
                    });
                }

                if (max_digits !== null && max_decimal_places !== null) {
                    var max_whole_digits = max_digits - max_decimal_places;
                    if (match[1].length > max_whole_digits) {
                        throw new ValidationError(msgs['max_whole_digits'], {
                            '%s': max_whole_digits
                        });
                    }
                }
            }
        },

        is_float: function(field, arg, value, msgs) {
            value = $.trim(value);
            if (!IS_FLOAT.test(value) || isNaN(parseFloat(value))) {
                throw new ValidationError(msgs['invalid']);
            }
        },

        is_integer: function(field, arg, value, msgs) {
            value = $.trim(value);
            if (!IS_INTEGER.test(value) || isNaN(parseInt(value))) {
                throw new ValidationError(msgs['invalid']);
            }
        },

        is_date: function(field, arg, value, msgs) {
            var is_date = new RegExp(IS_DATE);
            if (!is_date.test($.trim(value))) {
                throw new ValidationError(msgs['invalid']);
            }
        },

        is_datetime: function(field, arg, value, msgs) {
            var is_datetime = new RegExp(IS_DATETIME);
            if (!is_datetime.test($.trim(value))) {
                throw new ValidationError(msgs['invalid']);
            }
        },

        is_time: function(field, arg, value, msgs) {
            var is_time = new RegExp(IS_TIME);
            if (!is_time.test($.trim(value))) {
                throw new ValidationError(msgs['invalid']);
            }
        },

        max_value: function(field, arg, value, msgs) {
            var value = Number(value);
            if (value > arg) {
                throw new ValidationError(msgs['max_value'], {
                    '%(limit_value)s': arg
                });
            }
        },

        min_value: function(field, arg, value, msgs) {
            var value = Number(value);
            if (value < arg) {
                throw new ValidationError(msgs['min_value'], {
                    '%(limit_value)s': arg
                });
            }
        },

        regex: function(field, arg, value, msgs) {
            var re = RegExp(arg[0], arg[1]);
            if (!re.test(value)) {
                throw new ValidationError(msgs['invalid']);
            }
        },

        equal_to_field: function(field, arg, value, msgs) {
            var other = $(field.form).find(':input[name='+arg+']').val();
            if (other != value) {
                throw new ValidationError(msgs['equal_to_field']);
            }
        }

    });

})(jQuery);
