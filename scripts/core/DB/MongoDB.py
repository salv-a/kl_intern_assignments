class Course_revenue:
    dept_revenue = [
        {
            '$addFields': {
                '_id': 0,
                'course_fee': {
                    '$add': [
                        '$course_fee', 0
                    ]
                },
                'totaL_val': {
                    '$subtract': [
                        '$total_count', '$seats_left'
                    ]
                }
            }
        }, {
            '$addFields': {
                'revenue': {
                    '$multiply': [
                        '$totaL_val', '$course_fee'
                    ]
                }
            }
        }
    ]


class College_revenue:
    total_revenue = [
        {
            '$addFields': {
                '_id': 0,
                'course_fee': {
                    '$add': [
                        '$course_fee', 0
                    ]
                },
                'totaL_val': {
                    '$subtract': [
                        '$total_count', '$seats_left'
                    ]
                }
            }
        }, {
            '$addFields': {
                'revenue': {
                    '$multiply': [
                        '$totaL_val', '$course_fee'
                    ]
                }
            }
        }, {
            '$group': {
                '_id': 0,
                'total_revenue': {
                    '$sum': '$revenue'
                }
            }
        }
    ]

class coures_data:
    civil_data={
        'course_id': 'LxDsn'
    }
