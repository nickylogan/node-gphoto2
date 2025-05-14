{
  'targets': [
    {
      'target_name': 'gphoto2',
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
        "<!(pkg-config --cflags-only-I libgphoto2 | sed 's/-I//g')"
      ],
      'sources': [
        'src/autodetect.cc',
        'src/binding.cc',
        'src/camera.cc',
        'src/camera_helpers.cc',
        'src/gphoto.cc'
      ],
      'link_settings': {
        'libraries': [
          "<!(pkg-config --libs libgphoto2)"
        ]
      },
      'cflags': [
        '--std=c++20'
      ],
      'cflags!': [
        '-fno-exceptions'
      ],
      'target_arch': 'x64',
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CPLUSPLUSFLAGS' : [
              '-std=c++20',
              '-stdlib=libc++'
            ]
          }
        }]
      ]
    }
  ]
}
