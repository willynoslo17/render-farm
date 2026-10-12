import React from 'react';
import { Composition } from 'remotion';
import { Promo, PromoProps } from './Promo';

const defaults: PromoProps = {
  title: 'Your product',
  subtitle: 'Fast delivery',
  imageUrl: '',
  durationInFrames: 150,
};

export const Root: React.FC = () => (
  <Composition
    id="Promo"
    component={Promo}
    width={1080}
    height={1920}
    fps={30}
    durationInFrames={150}
    defaultProps={defaults}
    calculateMetadata={({ props }) => ({
      durationInFrames: Math.max(30, Math.min(1800, Number(props.durationInFrames) || 150)),
    })}
  />
);
