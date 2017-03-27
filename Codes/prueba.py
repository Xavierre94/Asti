require 'adafruit-servo-driver'

pwm = PWM.new(0x40, true)
pwm.set_pwm_freq(50)

channel = 0

3.times do
  pwm.set_pwm(channel, 0, 212)
  sleep(0.5)
  pwm.set_pwm(channel, 0, 412)
  sleep(0.5)
end
